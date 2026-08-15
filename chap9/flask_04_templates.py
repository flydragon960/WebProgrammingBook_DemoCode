# flask_04_templates.py
# Section: Templates
# Demonstrates: render_template, passing variables, Jinja2 control structures
# Requires: templates/base.html, templates/index.html, templates/users.html
#           templates/about.html
# Run: python flask_04_templates.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home", name="Alice")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/users")
def users():
    user_list = ["alice", "bob", "charlie"]
    return render_template("users.html", users=user_list)

@app.route("/user/<username>")
def user_profile(username):
    return f"Profile: {username}"

if __name__ == "__main__":
    app.run(debug=True)
