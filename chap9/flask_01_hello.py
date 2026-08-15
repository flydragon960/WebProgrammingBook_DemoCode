# flask_01_hello.py
# Section: Setting Up a Flask Project
# Demonstrates: minimal Flask app, @app.route, app.run
# Run: python flask_01_hello.py
# Visit: http://127.0.0.1:5000

from flask import Flask

app = Flask(__name__)    # create the Flask application object

@app.route("/")          # register the URL route "/"
def index():
    return "Hello, World!"   # return the HTTP response body

if __name__ == "__main__":
    app.run(debug=True)      # start the development server
