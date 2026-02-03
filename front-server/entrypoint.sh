#!/bin/sh
set -eu

cat > /app/config.js <<EOF
window.__APP_CONFIG__ = {
  API_URL: "/api",
  EVENTS_URL: "/events"
};
EOF

exec python3 -m http.server $FRONT_PORT
