from flask import Flask
app = Flask(__name__) # create the Flask application object @app.route("/") # register the URL route "/"
@app.route("/")
def index():
    return "Hello, World!" # return the HTTP response body
if __name__ == "__main__":
    app.run(debug=True)