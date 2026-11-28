"""Cryptographic primitives for Mitsubishi Motors IDM and Kintaro protocols."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time
from dataclasses import dataclass

from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_der_public_key

from .config import RegionConfig


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def make_device_jwt(
    jwt_sign_key: str,
    *,
    now: int | None = None,
    ttl_seconds: int = 3600,
) -> str:
    """Create the HS256 JWT used for `app-device-token` / `knt-app-device-token`."""
    iat = int(time.time()) if now is None else now
    header = _b64url(
        json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode()
    )
    payload = _b64url(
        json.dumps({"iat": iat, "exp": iat + ttl_seconds}, separators=(",", ":")).encode()
    )
    signing_input = f"{header}.{payload}".encode("ascii")
    sig = hmac.new(jwt_sign_key.encode("utf-8"), signing_input, hashlib.sha256).digest()
    return f"{header}.{payload}.{_b64url(sig)}"


def aes_ecb_encrypt(plaintext: str, key: bytes) -> str:
    """AES-256-ECB + PKCS7 + Base64 for IDM payloads."""
    padder = sym_padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode("utf-8")) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    enc = cipher.encryptor()
    ct = enc.update(padded) + enc.finalize()
    return base64.b64encode(ct).decode("ascii")


def aes_ecb_decrypt(b64_ciphertext: str, key: bytes) -> str:
    """Decrypt AES-256-ECB + PKCS7 + Base64 IDM response payload."""
    ct = base64.b64decode(b64_ciphertext)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    dec = cipher.decryptor()
    padded = dec.update(ct) + dec.finalize()
    unpadder = sym_padding.PKCS7(128).unpadder()
    pt = unpadder.update(padded) + unpadder.finalize()
    return pt.decode("utf-8")


def rsa_encrypt_password(password: str, key_index: str, b64_der_pubkey: str) -> str:
    """Encrypt login password as `<keyIndex>@<base64(RSA_PKCS1v15(password))>`."""
    pub = load_der_public_key(base64.b64decode(b64_der_pubkey))
    ct = pub.encrypt(password.encode("utf-8"), asym_padding.PKCS1v15())
    return f"{key_index}@{base64.b64encode(ct).decode('ascii')}"


def idm_signature(client_id: str, nonce: str, timestamp_ms: str) -> str:
    """Compute `X-Signature = md5(clientId + nonce + timestamp)` (lowercase hex)."""
    return hashlib.md5(f"{client_id}{nonce}{timestamp_ms}".encode("utf-8")).hexdigest()


def aes_cbc_encrypt(plaintext: str, key: bytes, iv: bytes) -> str:
    """AES-128-CBC + PKCS7 + Base64 for Kintaro requests."""
    padder = sym_padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode("utf-8")) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    enc = cipher.encryptor()
    ct = enc.update(padded) + enc.finalize()
    return base64.b64encode(ct).decode("ascii")


def aes_cbc_decrypt(b64_ciphertext: str, key: bytes, iv: bytes) -> str:
    """Decrypt AES-128-CBC + PKCS7 + Base64 Kintaro response payload."""
    ct = base64.b64decode(b64_ciphertext)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    dec = cipher.decryptor()
    padded = dec.update(ct) + dec.finalize()
    unpadder = sym_padding.PKCS7(128).unpadder()
    pt = unpadder.update(padded) + unpadder.finalize()
    return pt.decode("utf-8")


@dataclass(frozen=True)
class KintaroInitMaterial:
    init_key: bytes
    secret_part: str


def derive_kintaro_init_material(cfg: RegionConfig) -> KintaroInitMaterial:
    """Derive handshake AES key and signing secret from regional config."""
    m1 = (
        hashlib.md5(f"{cfg.kintaro_app_code}{cfg.package_name}".encode("ascii"))
        .hexdigest()
        .upper()
    )
    m2 = (
        hashlib.md5(f"{m1}{cfg.kintaro_app_hash}".encode("ascii"))
        .hexdigest()
        .lower()
    )
    s = cfg.kintaro_sec_cfg
    init_key = m2[s[0] : s[1]].encode("ascii")
    secret_part = m2[s[2] : s[3]] + m2[s[4] : s[5]] + m2[s[6] : s[7]]
    return KintaroInitMaterial(init_key=init_key, secret_part=secret_part)


def kintaro_init_sign(timestamp_ms: str, secret_part: str, cfg: RegionConfig) -> str:
    """Compute `knt-sign` for `POST /service/checkVersion`."""
    s = cfg.kintaro_sec_cfg
    tail = timestamp_ms[s[8] :] + timestamp_ms[s[9] :]
    return (
        hashlib.sha256(f"{timestamp_ms}{tail}{secret_part}".encode("ascii"))
        .hexdigest()
        .upper()
    )


def kintaro_normal_sign(
    encrypted_data: str,
    timestamp_ms: str,
    sign_key: str,
    cfg: RegionConfig,
) -> str:
    """Compute `knt-sign` for normal encrypted Kintaro requests."""
    s = cfg.kintaro_sec_cfg
    tail = timestamp_ms[s[8] :] + timestamp_ms[s[9] :]
    return (
        hashlib.sha256(f"{encrypted_data}{timestamp_ms}{tail}{sign_key}".encode("utf-8"))
        .hexdigest()
        .upper()
    )


def generate_client_nonce() -> str:
    """Generate a 32-byte random Base64 nonce for PIN challenge."""
    return base64.b64encode(os.urandom(32)).decode("ascii")


def compute_pin_hash(pin: str, client_nonce: str, server_nonce: str) -> str:
    """Compute folded 16-byte HMAC-SHA256 PIN hash."""
    key = base64.b64decode(client_nonce) + b":" + base64.b64decode(server_nonce)
    digest = hmac.new(key, pin.encode("utf-8"), hashlib.sha256).digest()
    folded = bytes(digest[i] ^ digest[i + 16] for i in range(16))
    return base64.b64encode(folded).decode("ascii")
