# flask_10_error_handling.py
# Section: Error Handling
# Demonstrates: @app.errorhandler for 404, 401, 500 with JSON responses
# Run: python flask_10_error_handling.py
#
# Test:
#   404: curl http://127.0.0.1:5000/nonexistent
#   401: curl http://127.0.0.1:5000/protected
#   500: curl http://127.0.0.1:5000/crash

from flask import Flask, jsonify, abort

app = Flask(__name__)

# ------------------------------------------------------------------
# Custom error handlers
# ------------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(401)
def unauthorized(e):
    return jsonify({"error": "Authentication required"}), 401

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# ------------------------------------------------------------------
# Demo routes that trigger each error
# ------------------------------------------------------------------
@app.route("/")
def index():
    return jsonify({"message": "OK"})

@app.route("/protected")
def protected():
    abort(401)   # triggers the 401 handler

@app.route("/crash")
def crash():
    raise RuntimeError("Simulated server crash")   # triggers 500 handler

if __name__ == "__main__":
    app.run(debug=False)   # debug=False so 500 handler fires instead of debugger
