#!/usr/bin/env bash
# Start the Django dev server on the first free port >= 8000 (or $PORT if set),
# so parallel workspaces don't collide.
set -euo pipefail

WS="${SUPERSET_WORKSPACE_PATH:-$(cd "$(dirname "$0")/.." && pwd)}"
cd "$WS"

if [ ! -x .venv/bin/python ]; then
  echo "No .venv found; running setup first"
  ./.superset/setup.sh
fi

PORT="${PORT:-$(.venv/bin/python - <<'PY'
import socket
for p in range(8000, 8100):
    s = socket.socket()
    try:
        s.bind(("127.0.0.1", p))
    except OSError:
        continue
    finally:
        s.close()
    print(p)
    break
else:
    raise SystemExit("no free port in 8000-8099")
PY
)}"

# Bind 127.0.0.1 (it's in ALLOWED_HOSTS; "localhost" is not).
echo "Starting dev server at http://127.0.0.1:$PORT/"
exec .venv/bin/python "$WS/manage.py" runserver "127.0.0.1:$PORT"
