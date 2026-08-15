# flask_11_blueprints_app.py
# Section: Blueprints - Organising a Larger Application
# Demonstrates: register_blueprint, url_prefix, modular route organisation
# Requires: auth.py, api.py (in the same directory)
# Run: python flask_11_blueprints_app.py
#
# Routes registered:
#   POST /auth/login
#   POST /auth/register
#   GET  /api/items
#   GET  /api/status
#
# Test:
#   curl -X POST http://127.0.0.1:5000/auth/login \
#        -H "Content-Type: application/json" \
#        -d '{"username": "alice", "password": "password123"}'
#
#   curl http://127.0.0.1:5000/api/items

import os
from flask import Flask
from auth import auth_bp
from api  import api_bp

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

app.register_blueprint(auth_bp)   # mounts at /auth
app.register_blueprint(api_bp)    # mounts at /api

if __name__ == "__main__":
    app.run(debug=True)
