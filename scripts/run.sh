#!/bin/sh

WORKER_TIMEOUT="${WORKER_TIMEOUT:-160}"

uvicorn \
      --workers 1 \
      --timeout-keep-alive "$WORKER_TIMEOUT" \
      --log-level 'info'\
      src.main:app --reload --host 0.0.0.0 --port 9001