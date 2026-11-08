# flask_08b_jwt_api.py
# Section: JSON Web Tokens - login API and protected routes
# Demonstrates: token-based login, @token_required decorator, Bearer header
# Install: pip install flask PyJWT
# Requires: flask_08a_jwt_helpers.py (in the same folder)
# Run: python flask_08b_jwt_api.py
#
# Test with curl:
#   Login:
#     curl -X POST http://127.0.0.1:5000/api/login \
#          -H "Content-Type: application/json" \
#          -d '{"username": "alice", "password": "password123"}'
#
#   Access protected route (replace <token> with value from login):
#     curl http://127.0.0.1:5000/api/profile \
#          -H "Authorization: Bearer <token>"

from functools import wraps
from flask import Flask, request, jsonify
from flask_08a_jwt_helpers import create_token, verify_token   # reuse 8a

app = Flask(__name__)

# ------------------------------------------------------------------
# Simulated user store (use a real database with hashed passwords)
# ------------------------------------------------------------------
USERS = {
    1: {"username": "alice", "password": "password123"},
    2: {"username": "bob",   "password": "secret456"},
}

# ------------------------------------------------------------------
# @token_required decorator: protects any route with JWT auth
# ------------------------------------------------------------------
def token_required(f):
    """Decorator: protect a route with JWT authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing token"}), 401

        token = auth_header.split(" ", 1)[1]
        payload = verify_token(token)
        if payload is None:
            return jsonify({"error": "Invalid or expired token"}), 401

        return f(payload, *args, **kwargs)   # pass payload to view
    return decorated


# ------------------------------------------------------------------
# Login endpoint: returns a JWT on valid credentials
# ------------------------------------------------------------------
@app.route("/api/login", methods=["POST"])
def api_login():
    data     = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    # Find the user by username
    user = next((u for u in USERS.values()
                 if u["username"] == username), None)

    if not user or user["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    user_id = next(k for k, v in USERS.items()
                   if v["username"] == username)
    token = create_token(user_id, username)
    return jsonify({"token": token}), 200


# ------------------------------------------------------------------
# Protected routes: require valid Bearer token
# ------------------------------------------------------------------
@app.route("/api/profile", methods=["GET"])
@token_required
def api_profile(payload):
    return jsonify({
        "user_id":  int(payload["sub"]),   # "sub" is stored as a string
        "username": payload["username"],
    })


@app.route("/api/secret", methods=["GET"])
@token_required
def api_secret(payload):
    return jsonify({
        "message": f"Hello {payload['username']}, here is your secret data."
    })


if __name__ == "__main__":
    app.run(debug=True)
