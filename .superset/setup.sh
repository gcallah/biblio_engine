#!/usr/bin/env bash
# Prepare a fresh Superset workspace: venv + deps, and untracked files from the main checkout.
set -euo pipefail

WS="${SUPERSET_WORKSPACE_PATH:-$(pwd)}"
ROOT="${SUPERSET_ROOT_PATH:-}"
cd "$WS"

# 1. Per-workspace virtualenv (idempotent).
if [ ! -x .venv/bin/python ]; then
  echo "Creating virtualenv in .venv"
  python3 -m venv .venv
fi
.venv/bin/python -m pip install --quiet --upgrade pip
.venv/bin/python -m pip install --quiet -r requirements/requirements.txt

# 2. Copy untracked/gitignored files from the main checkout (never overwrite).
copy_if_missing() {
  local rel="$1"
  if [ -f "$ROOT/$rel" ] && [ ! -e "$WS/$rel" ]; then
    mkdir -p "$(dirname "$WS/$rel")"
    cp "$ROOT/$rel" "$WS/$rel"
    echo "Copied $rel from main checkout"
  fi
}

if [ -n "$ROOT" ] && [ -d "$ROOT" ] && [ "$ROOT" != "$WS" ]; then
  # Env files (none today, but picked up automatically if added).
  for f in "$ROOT"/.env "$ROOT"/.env.*; do
    [ -f "$f" ] && copy_if_missing "$(basename "$f")"
  done
  # db.sqlite3 is not in git (the live database is the master copy); work
  # on a copy of the main checkout's, or fetch the live one with
  # bin/pull_live_db.sh.
  copy_if_missing db.sqlite3
  # Migrations are gitignored but db.sqlite3 already records them;
  # without these, makemigrations would generate a conflicting 0001.
  for f in "$ROOT"/berkeley/migrations/*.py; do
    [ -f "$f" ] && copy_if_missing "berkeley/migrations/$(basename "$f")"
  done
else
  echo "SUPERSET_ROOT_PATH not set or same as workspace; skipping file copy"
fi

# 3. Smoke test. (No migrate here: apply migrations deliberately.)
.venv/bin/python manage.py check
echo "Setup complete. Use the Run button (or ./.superset/run.sh) to start the dev server."
