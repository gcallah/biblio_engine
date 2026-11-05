#!/usr/bin/env bash
# Stop this workspace's dev server (runserver + its autoreload child). Setup starts nothing else.
WS="${SUPERSET_WORKSPACE_PATH:-$(pwd)}"
pkill -f "$WS/manage.py runserver" 2>/dev/null && echo "Stopped dev server for $WS" || echo "No dev server running"
exit 0
