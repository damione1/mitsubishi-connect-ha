#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${ROOT_DIR}/generated/mitsubishi_connect_api"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

# openapi.yaml is OpenAPI 3.2; openapi-python-client only reads 3.1.x.
uv run --no-project --with pyyaml python "${ROOT_DIR}/scripts/downgrade_openapi.py" \
  "${ROOT_DIR}/openapi/openapi.yaml" "${TMP_DIR}/openapi.yaml"

rm -rf "${OUT_DIR}"
uvx openapi-python-client generate \
  --path "${TMP_DIR}/openapi.yaml" \
  --config "${ROOT_DIR}/openapi/client-config.yaml" \
  --output-path "${OUT_DIR}" \
  --meta uv \
  --overwrite

echo "Generated OpenAPI Python client in ${OUT_DIR}"
