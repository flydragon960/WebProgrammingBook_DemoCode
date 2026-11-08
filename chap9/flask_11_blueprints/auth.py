# auth.py  --  authentication blueprint
# Section: Blueprints
# Demonstrates: Blueprint definition, url_prefix, route registration
# Used by: flask_11_blueprints_app.py

from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data     = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")

    # Simplified check (use hashed passwords and a real database)
    if username == "alice" and password == "password123":
        return jsonify({"token": "demo-token-for-alice"})
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/register", methods=["POST"])
def register():
    data     = request.get_json() or {}
    username = data.get("username", "")
    if not username:
        return jsonify({"error": "Username required"}), 400
    return jsonify({"message": f"User '{username}' registered"}), 201
