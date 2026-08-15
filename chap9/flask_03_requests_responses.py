# flask_03_requests_responses.py
# Section: HTTP Requests and Responses
# Demonstrates: request object, query strings, response types,
#               jsonify, GET/POST handling
# Run: python flask_03_requests_responses.py

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# ------------------------------------------------------------------
# Request object: method, user_agent, remote_addr, args
# Visit: http://127.0.0.1:5000/info
# ------------------------------------------------------------------
@app.route("/info")
def info():
    method = request.method          # "GET", "POST", etc.
    ua     = request.user_agent      # browser / client info
    ip     = request.remote_addr     # client IP address
    args   = request.args            # query string parameters (dict)
    return f"Method: {method}, IP: {ip}, UA: {ua}"

# ------------------------------------------------------------------
# Query string parameters
# Visit: http://127.0.0.1:5000/search?q=python&page=2
# ------------------------------------------------------------------
@app.route("/search")
def search():
    query = request.args.get("q", "")        # default "" if not present
    page  = request.args.get("page", 1, type=int)
    return f"Searching for '{query}', page {page}"

# ------------------------------------------------------------------
# Returning different response types
# ------------------------------------------------------------------
@app.route("/ok")
def ok():
    return "Success", 200                    # body + status code

@app.route("/not-found")
def not_found_demo():
    return "Page not found", 404

@app.route("/custom-header")
def custom_header():
    resp = make_response("Custom response")
    resp.headers["X-Custom"] = "MyValue"     # add a custom header
    return resp

# ------------------------------------------------------------------
# JSON responses
# Visit: http://127.0.0.1:5000/api/user
# ------------------------------------------------------------------
@app.route("/api/user")
def api_user():
    user = {"id": 1, "name": "Alice", "email": "alice@example.com"}
    return jsonify(user)            # HTTP 200 + JSON body

@app.route("/api/users")
def api_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    return jsonify(users), 200

# ------------------------------------------------------------------
# Handling GET and POST on the same route
# GET:  http://127.0.0.1:5000/api/items
# POST: curl -X POST http://127.0.0.1:5000/api/items \
#            -H "Content-Type: application/json" \
#            -d '{"name": "cherry"}'
# ------------------------------------------------------------------
@app.route("/api/items", methods=["GET", "POST"])
def items():
    if request.method == "GET":
        return jsonify({"items": ["apple", "banana"]})

    if request.method == "POST":
        data = request.get_json()           # parse JSON request body
        name = data.get("name", "")
        return jsonify({"created": name}), 201

if __name__ == "__main__":
    app.run(debug=True)
