# flask_06_cookies.py
# Section: Cookies
# Demonstrates: set_cookie, request.cookies, delete_cookie, security attributes
# Run: python flask_06_cookies.py

from flask import Flask, request, make_response

app = Flask(__name__)

# ------------------------------------------------------------------
# Set a cookie
# Visit: http://127.0.0.1:5000/set-theme
# ------------------------------------------------------------------
@app.route("/set-theme")
def set_theme():
    resp = make_response("Theme set to dark.")
    resp.set_cookie(
        "theme",               # cookie name
        "dark",                # cookie value
        max_age=60*60*24*30,   # expires in 30 days (seconds)
        httponly=True,         # not accessible via JavaScript (XSS protection)
        samesite="Lax"         # restrict cross-site sending (CSRF protection)
        # secure=True          # uncomment in production (HTTPS only)
    )
    return resp

# ------------------------------------------------------------------
# Read a cookie
# Visit: http://127.0.0.1:5000/get-theme
# ------------------------------------------------------------------
@app.route("/get-theme")
def get_theme():
    theme = request.cookies.get("theme", "light")   # default "light"
    return f"Current theme: {theme}"

# ------------------------------------------------------------------
# Delete a cookie
# Visit: http://127.0.0.1:5000/clear-theme
# ------------------------------------------------------------------
@app.route("/clear-theme")
def clear_theme():
    resp = make_response("Theme cleared.")
    resp.delete_cookie("theme")
    return resp

if __name__ == "__main__":
    app.run(debug=True)
