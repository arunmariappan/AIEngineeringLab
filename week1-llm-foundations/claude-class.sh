#!/usr/bin/env bash
# Start Claude Code with your CLASS key and the course model (Haiku 5.5).
# Reads .env next to this script. Changes nothing in your own Claude Code setup,
# and never prints your key. Extra arguments pass through, e.g.:
#   bash claude-class.sh --permission-mode plan
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -f .env ]; then
  echo "No .env file here. Copy .env.example to .env and paste your class key first."
  exit 1
fi
set -a; . <(tr -d '\r' < .env); set +a   # tolerate Windows line endings in .env
if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "Your .env has no ANTHROPIC_API_KEY line. Paste your class key into .env first."
  exit 1
fi
# Through the class gateway the key travels as a bearer token; direct keys stay as they are.
if [ -n "${ANTHROPIC_BASE_URL:-}" ]; then
  export ANTHROPIC_AUTH_TOKEN="$ANTHROPIC_API_KEY"
  unset ANTHROPIC_API_KEY
fi
export ANTHROPIC_MODEL=claude-haiku-5-5
exec claude "$@"
