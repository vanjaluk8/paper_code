#!/usr/bin/env bash
#
# compile_mdpi.sh — Compile the MDPI manuscript with a Docker TeX Live image.
#
# Minimal: mount the manuscript dir, build a writable copy inside the
# container (the MDPI class writes Definitions/*-converted-to.pdf during EPS
# conversion, so the source mount is read-only and we copy first), then hand
# the finished PDF back to an output dir on the host.
#
# Usage:
#   ./compile_mdpi.sh [OUTPUT_DIR]
#
# Requires Definitions/logo-orcid.pdf to be present in the manuscript tree
# (mdpi.cls uses it). Default output: ./build/out/main.pdf

set -euo pipefail

IMAGE="${MDPI_IMAGE:-texlive/texlive:latest}"
ROOT="$(pwd)"
OUT_DIR="${1:-$ROOT/build/out}"

# We must be in the manuscript root (the dir with main.tex).
if [[ ! -f "$ROOT/main.tex" ]]; then
  echo "ERROR: run this from the manuscript directory containing main.tex" >&2
  exit 1
fi
if ! command -v docker >/dev/null 2>&1; then
  echo "ERROR: docker not found on PATH" >&2; exit 2
fi
docker image inspect "$IMAGE" >/dev/null 2>&1 || {
  echo "ERROR: docker image '$IMAGE' not present. Pull it first:" >&2
  echo "       docker pull $IMAGE" >&2
  exit 2
}
if [[ ! -f "$ROOT/Definitions/logo-orcid.pdf" ]]; then
  echo "ERROR: Definitions/logo-orcid.pdf is missing (mdpi.cls requires it)." >&2
  exit 2
fi

mkdir -p "$OUT_DIR"

echo "[compile] Building $ROOT/main.tex ..."
echo "[compile] Output -> $OUT_DIR/main.pdf"

docker run --rm \
  -v "$ROOT":/src:ro \
  -v "$OUT_DIR":/out \
  -w /tmp \
  "$IMAGE" \
  sh -c 'mkdir -p /tmp/w && cp -a /src/. /tmp/w && cd /tmp/w \
         && latexmk -pdf -shell-escape -interaction=nonstopmode -halt-on-error main.tex \
         && cp main.pdf /out/main2.pdf'

echo "[compile] Done: $OUT_DIR/main2.pdf"
