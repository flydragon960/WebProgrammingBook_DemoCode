# ch08_12_flask_sessions.py
# Section: Sessions, Cookies, and Tokens - Sessions
# Topics: Flask session, secret_key, login/logout routes
# Install: pip install flask
# Run:     python ch08_12_flask_sessions.py

from flask import Flask, session

app = Flask(__name__)
app.secret_key = "secret"    # use a long random string in production

@app.route("/login")
def login():
    session["user"] = "Alice"    # store data server-side
    return "Logged in."

@app.route("/logout")
def logout():
    session.pop("user", None)    # remove the key; None prevents KeyError
    return "Logged out."

@app.route("/profile")
def profile():
    user = session.get("user")
    if user:
        return f"Logged in as {user}."
    return "Not logged in.", 401

if __name__ == "__main__":
    app.run(debug=True)
