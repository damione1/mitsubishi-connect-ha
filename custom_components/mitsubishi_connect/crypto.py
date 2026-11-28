"""Cryptographic helpers for Mitsubishi Connect (IDM & Kintaro)."""

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

from .regions import RegionProfile


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def make_device_jwt(jwt_sign_key: str, *, ttl_seconds: int = 3600) -> str:
    iat = int(time.time())
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
    padder = sym_padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode("utf-8")) + padder.finalize()
    enc = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    return base64.b64encode(enc.update(padded) + enc.finalize()).decode("ascii")


def aes_ecb_decrypt(b64_ciphertext: str, key: bytes) -> str:
    ct = base64.b64decode(b64_ciphertext)
    dec = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
    padded = dec.update(ct) + dec.finalize()
    unpadder = sym_padding.PKCS7(128).unpadder()
    return (unpadder.update(padded) + unpadder.finalize()).decode("utf-8")


def rsa_encrypt_password(password: str, key_index: str, b64_der_pubkey: str) -> str:
    pub = load_der_public_key(base64.b64decode(b64_der_pubkey))
    ct = pub.encrypt(password.encode("utf-8"), asym_padding.PKCS1v15())
    return f"{key_index}@{base64.b64encode(ct).decode('ascii')}"


def idm_signature(client_id: str, nonce: str, timestamp_ms: str) -> str:
    return hashlib.md5(f"{client_id}{nonce}{timestamp_ms}".encode("utf-8")).hexdigest()


def aes_cbc_encrypt(plaintext: str, key: bytes, iv: bytes) -> str:
    padder = sym_padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode("utf-8")) + padder.finalize()
    enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    return base64.b64encode(enc.update(padded) + enc.finalize()).decode("ascii")


def aes_cbc_decrypt(b64_ciphertext: str, key: bytes, iv: bytes) -> str:
    ct = base64.b64decode(b64_ciphertext)
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    padded = dec.update(ct) + dec.finalize()
    unpadder = sym_padding.PKCS7(128).unpadder()
    return (unpadder.update(padded) + unpadder.finalize()).decode("utf-8")


@dataclass(frozen=True)
class KintaroInitMaterial:
    init_key: bytes
    secret_part: str


def derive_kintaro_init_material(cfg: RegionProfile) -> KintaroInitMaterial:
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
    return KintaroInitMaterial(
        init_key=m2[s[0] : s[1]].encode("ascii"),
        secret_part=m2[s[2] : s[3]] + m2[s[4] : s[5]] + m2[s[6] : s[7]],
    )


def kintaro_init_sign(ts: str, secret_part: str, cfg: RegionProfile) -> str:
    s = cfg.kintaro_sec_cfg
    tail = ts[s[8] :] + ts[s[9] :]
    return hashlib.sha256(f"{ts}{tail}{secret_part}".encode("ascii")).hexdigest().upper()


def kintaro_normal_sign(enc_data: str, ts: str, sign_key: str, cfg: RegionProfile) -> str:
    s = cfg.kintaro_sec_cfg
    tail = ts[s[8] :] + ts[s[9] :]
    return (
        hashlib.sha256(f"{enc_data}{ts}{tail}{sign_key}".encode("utf-8"))
        .hexdigest()
        .upper()
    )


def generate_client_nonce() -> str:
    return base64.b64encode(os.urandom(32)).decode("ascii")


def compute_pin_hash(pin: str, client_nonce: str, server_nonce: str) -> str:
    key = base64.b64decode(client_nonce) + b":" + base64.b64decode(server_nonce)
    digest = hmac.new(key, pin.encode("utf-8"), hashlib.sha256).digest()
    folded = bytes(digest[i] ^ digest[i + 16] for i in range(16))
    return base64.b64encode(folded).decode("ascii")
