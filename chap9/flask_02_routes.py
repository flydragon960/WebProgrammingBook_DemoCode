# flask_02_routes.py
# Section: Routes and URL Building
# Demonstrates: static routes, dynamic URL segments, type converters, url_for()
# Run: python flask_02_routes.py

from flask import Flask, url_for

app = Flask(__name__)

# ------------------------------------------------------------------
# Static routes
# ------------------------------------------------------------------
@app.route("/")
def index():
    return "Home page"

@app.route("/about")
def about():
    return "About page"

@app.route("/contact")
def contact():
    return "Contact page"

# ------------------------------------------------------------------
# Dynamic routes with URL parameters
# ------------------------------------------------------------------
@app.route("/user/<username>")          # string segment (default)
def user_profile(username):
    return f"Profile page for: {username}"

@app.route("/post/<int:post_id>")       # int converter
def show_post(post_id):
    return f"Post number: {post_id}"    # post_id is already an int

# ------------------------------------------------------------------
# url_for() demo (run outside request context using test_request_context)
# ------------------------------------------------------------------
with app.test_request_context():
    print(url_for("user_profile", username="alice"))   # /user/alice
    print(url_for("user_profile", username="bob"))     # /user/bob
    print(url_for("show_post", post_id=42))            # /post/42

if __name__ == "__main__":
    app.run(debug=True)
