# ai_era/generated_hello.py
# Section: Flask Code in the AI Era -- the AI's version (DO NOT DEPLOY)
# Three defects: debugger on, hard-coded secret, unescaped user input (XSS)
# Run:  python generated_hello.py
# Try:  http://127.0.0.1:5000/hello?name=Ada
#       http://127.0.0.1:5000/hello?name=<script>alert(1)</script>   <-- runs!

from flask import Flask, request, render_template_string
app = Flask(__name__)
app.secret_key = "secret123"                       # hard-coded secret

@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    return render_template_string("<h1>Hello " + name + "</h1>")  # XSS

if __name__ == "__main__":
    app.run(debug=True)                            # debugger exposed
