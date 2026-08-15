# flask_12_production_config.py
# Section: Deploying to Production
# Demonstrates: loading secrets from environment variables, never hard-coding
# Run: python flask_12_production_config.py
#
# Set environment variables before running (macOS/Linux):
#   export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
#   export JWT_SECRET="$(python -c 'import secrets; print(secrets.token_hex(32))')"
#   python flask_12_production_config.py
#
# Production server (after setting env vars):
#   gunicorn --workers 4 --bind 127.0.0.1:8000 flask_12_production_config:app

import os
from flask import Flask, jsonify

app = Flask(__name__)

# Load secrets from environment variables; fall back to dev values only locally
app.secret_key = os.environ.get("SECRET_KEY", "fallback-dev-key-change-in-production")
JWT_SECRET     = os.environ.get("JWT_SECRET", "fallback-jwt-key-change-in-production")

@app.route("/")
def index():
    return jsonify({
        "message": "App is running",
        "debug":   app.debug,
        "secret_key_set": app.secret_key != "fallback-dev-key-change-in-production",
    })

if __name__ == "__main__":
    # Development only: never run with debug=True in production
    app.run(debug=True, host="127.0.0.1", port=5000)
