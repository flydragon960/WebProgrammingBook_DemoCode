# ch08_14_fastapi_auth.py
# Section: Multiple Users and Authentication Flow
# Topics: FastAPI, OAuth2PasswordBearer, Depends, HTTPException, JWT
# Install: pip install fastapi uvicorn PyJWT
# Run:     uvicorn ch08_14_fastapi_auth:app --reload

import jwt
import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET = "key123"    # use a long random string in production

def create_token(user):
    payload = {
        "user": user,
        "exp": datetime.datetime.now(datetime.timezone.utc)
               + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.get("/token-demo")
def get_demo_token():
    """Helper endpoint: returns a valid token for testing."""
    return {"token": create_token("Alice")}

@app.get("/profile")
def read_profile(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)       # decode and validate the JWT
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    return {"user": user["user"]}    # return user data from token payload
