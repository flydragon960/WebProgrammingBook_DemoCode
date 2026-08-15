# ch08_11_flask_routes.py
# Section: HTTP Requests and Responses
# Topics: Flask routes, GET, POST, jsonify, request.get_json()
# Install: pip install flask
# Run:     python ch08_11_flask_routes.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return jsonify({"message": "GET request received"})
    else:
        data = request.get_json()     # parse the JSON body
        return jsonify({"received": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
