# flask_07_sessions.py
# Section: Sessions
# Demonstrates: session dict, secret_key, visit counter, login/logout flow
# Requires: templates/login.html
# Run: python flask_07_sessions.py

import secrets
from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-random-key"

# Generate a safe secret key (run once and store in environment variable):
# import secrets; print(secrets.token_hex(32))

# ------------------------------------------------------------------
# Basic session usage: visit counter
# Visit: http://127.0.0.1:5000/counter
# ------------------------------------------------------------------
@app.route("/counter")
def counter():
    visits = session.get("visits", 0)
    session["visits"] = visits + 1
    return f"You have visited this page {session['visits']} time(s)."

@app.route("/counter/clear")
def counter_clear():
    session.clear()    # remove all session data
    return "Session cleared."

# ------------------------------------------------------------------
# Simulated user database (use a real database in production)
# ------------------------------------------------------------------
USERS = {
    "alice": "password123",
    "bob":   "secret456",
}

# ------------------------------------------------------------------
# Login: GET renders form, POST authenticates and redirects
# Visit: http://127.0.0.1:5000/login
# ------------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if USERS.get(username) == password:
            session["username"] = username   # store in session
            session.permanent = True         # persist beyond browser close
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)

# ------------------------------------------------------------------
# Protected page: only accessible when logged in
# Visit: http://127.0.0.1:5000/dashboard
# ------------------------------------------------------------------
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))    # not logged in -> redirect
    return f"Welcome, {session['username']}! <a href='/logout'>Log out</a>"

# ------------------------------------------------------------------
# Logout: remove session data and redirect to login
# ------------------------------------------------------------------
@app.route("/logout")
def logout():
    session.pop("username", None)   # remove only the username key
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
