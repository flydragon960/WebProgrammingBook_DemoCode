# fastapi_auth.py
# Section: A Second Framework -- FastAPI
# Demonstrates: FastAPI routes, Depends, HTTPBearer, HTTPException, JWT
# Install: pip install fastapi uvicorn PyJWT
# Requires: flask_08a_jwt_helpers.py (in the same folder; it uses only PyJWT)
# Run:     uvicorn fastapi_auth:app --reload
# Try:     http://127.0.0.1:8000/docs   (interactive test page)
#
#   1. GET /token-demo                     -> copy the token
#   2. Click "Authorize", paste the token  (no "Bearer " prefix needed)
#   3. GET /profile                        -> {"user_id": 1, "username": "alice"}

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from flask_08a_jwt_helpers import create_token, verify_token   # reuse 8a

app = FastAPI()
bearer = HTTPBearer()          # reads "Authorization: Bearer <token>"


@app.get("/token-demo")
def get_demo_token():
    """Helper endpoint: returns a valid token for testing (no password!)."""
    return {"token": create_token(1, "alice")}


@app.get("/profile")
def read_profile(creds: HTTPAuthorizationCredentials = Depends(bearer)):
    payload = verify_token(creds.credentials)    # decode and validate the JWT
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"user_id": int(payload["sub"]), "username": payload["username"]}
