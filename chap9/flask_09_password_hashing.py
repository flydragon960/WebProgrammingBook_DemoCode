# flask_09_password_hashing.py
# Section: Password Hashing
# Demonstrates: bcrypt hash_password, check_password, register/login API
# Install: pip install flask bcrypt PyJWT
# Requires: flask_08a_jwt_helpers.py (in the same folder)
# Run: python flask_09_password_hashing.py
#
# Test with curl:
#   Register:
#     curl -X POST http://127.0.0.1:5000/api/register \
#          -H "Content-Type: application/json" \
#          -d '{"username": "alice", "password": "mypassword"}'
#
#   Login:
#     curl -X POST http://127.0.0.1:5000/api/login \
#          -H "Content-Type: application/json" \
#          -d '{"username": "alice", "password": "mypassword"}'

import bcrypt
from flask import Flask, request, jsonify
from flask_08a_jwt_helpers import create_token   # JWT helper from 8a

app = Flask(__name__)

# ------------------------------------------------------------------
# Password helpers
# ------------------------------------------------------------------
def hash_password(plaintext: str) -> str:
    """Hash a plaintext password. Returns a string safe for database storage."""
    salt   = bcrypt.gensalt(rounds=12)           # 2^12 hashing iterations
    hashed = bcrypt.hashpw(plaintext.encode(), salt)
    return hashed.decode("utf-8")


def check_password(plaintext: str, hashed: str) -> bool:
    """Return True if plaintext matches the stored hash."""
    return bcrypt.checkpw(plaintext.encode(), hashed.encode("utf-8"))


# ------------------------------------------------------------------
# Standalone hash demo (runs only when executed directly)
# ------------------------------------------------------------------
def _demo_hashing():
    stored = hash_password("mypassword")
    print("Hash:", stored)                              # $2b$12$...
    print("Correct:", check_password("mypassword",   stored))   # True
    print("Wrong:  ", check_password("wrongpassword", stored))  # False


# ------------------------------------------------------------------
# Simulated database (replace with a real database in production)
# ------------------------------------------------------------------
user_db = {}   # {"alice": {"id": 1, "password_hash": "..."}}
next_id  = 1


# ------------------------------------------------------------------
# Registration endpoint
# ------------------------------------------------------------------
@app.route("/api/register", methods=["POST"])
def register():
    global next_id
    data     = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if username in user_db:
        return jsonify({"error": "Username already taken"}), 409

    user_db[username] = {
        "id":            next_id,
        "password_hash": hash_password(password),   # never store plaintext
    }
    next_id += 1
    return jsonify({"message": "Registered successfully"}), 201


# ------------------------------------------------------------------
# Login endpoint
# ------------------------------------------------------------------
@app.route("/api/login", methods=["POST"])
def login():
    data     = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    user = user_db.get(username)
    if not user or not check_password(password, user["password_hash"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_token(user["id"], username)
    return jsonify({"token": token}), 200


if __name__ == "__main__":
    _demo_hashing()       # show bcrypt output in terminal
    app.run(debug=True)
