#!/bin/bash
# Installerar projektets beroenden i Claude Code på webben så att verktygen i
# tools/ fungerar direkt i en ny container. Idempotent, körs vid sessionsstart.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Python: Pillow krävs av build_index.py och generate_images.py.
python3 -m pip install --quiet --disable-pip-version-check pillow

# Node: docx (Word-underlag) och playwright-core (sidverifiering med
# /opt/pw-browsers/chromium, ladda aldrig ner egen webbläsare).
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
npm install --no-audit --no-fund --silent

echo "Akelius: beroenden klara (pillow, docx, playwright-core)"
