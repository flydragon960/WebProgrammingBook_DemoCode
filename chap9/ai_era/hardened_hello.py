# ai_era/hardened_hello.py
# Section: Flask Code in the AI Era -- the hardened version
# Requires: templates/hello.html; the SECRET_KEY environment variable
# Run (macOS/Linux):
#   export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
#   python hardened_hello.py
# Run (Windows PowerShell):
#   $env:SECRET_KEY = python -c "import secrets; print(secrets.token_hex(32))"
#   python hardened_hello.py

import os
from flask import Flask, request, render_template
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]          # 2. secret from env

@app.route("/hello")
def hello():
    name = request.args.get("name", "").strip()
    if not name:                                   # 1. validate input
        return "Name is required.", 400
    return render_template("hello.html", name=name)  # 1. autoescaped template

if __name__ == "__main__":
    app.run(debug=False)                           # 2. debugger off
