# api.py  --  application API blueprint
# Section: Blueprints
# Demonstrates: Blueprint definition, url_prefix
# Used by: flask_11_blueprints_app.py

from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/items")
def items():
    return jsonify({"items": ["apple", "banana", "cherry"]})

@api_bp.route("/status")
def status():
    return jsonify({"status": "ok", "version": "1.0"})
