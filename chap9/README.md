# Chapter 9: Server-Side Web Programming with Python — demo code

Open `index.html` in a browser for a guided page: each demo with its book section, the command to run it, what to try, and its source.

## Setup (once)

```bash
cd chap9
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run a Flask file with `python <file>.py` and open http://127.0.0.1:5000.
Files that use templates live in their own folder with a `templates/` subfolder,
the way a real Flask project is laid out: `cd` into that folder first.

| File | Book section |
|---|---|
| `flask_00_wsgi.py` | How a Python Web Application Runs (WSGI) — no framework; port 8000 |
| `flask_01_hello.py` | Setting Up a Flask Project |
| `flask_02_routes.py` | Routes and URL Building |
| `flask_03_requests_responses.py` | HTTP Requests and Responses |
| `flask_04_templates/` | Templates (Jinja2): rendering, control structures, inheritance |
| `flask_05_forms/` | Form Handling: validation, Post/Redirect/Get, file uploads |
| `flask_06_cookies.py` | Cookies |
| `flask_07_sessions/` | Sessions: visit counter, login and logout |
| `flask_08a_jwt_helpers.py` | JWT: creating and verifying tokens (also imported by 08b, 09 and `fastapi_auth.py`) |
| `flask_08b_jwt_api.py` | JWT: login API and the `@token_required` decorator |
| `flask_09_password_hashing.py` | Password Hashing with bcrypt |
| `flask_10_error_handling.py` | Error Handling |
| `flask_11_blueprints/` | Blueprints (`auth.py`, `api.py`, `flask_11_blueprints_app.py`) |
| `flask_12_production_config.py` | Configuration for Production |
| `fastapi_auth.py` | A Second Framework: FastAPI — run with `uvicorn fastapi_auth:app --reload` |
| `ai_era/` | Flask Code in the AI Era: `generated_hello.py` (insecure, do not deploy) and `hardened_hello.py` |

Note: PyJWT 2.10 and later require the `"sub"` claim to be a string, so
`create_token` stores `str(user_id)`.
