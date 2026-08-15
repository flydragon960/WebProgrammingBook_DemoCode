# ch08_13_jwt_tokens.py
# Section: Sessions, Cookies, and Tokens - JWT
# Topics: PyJWT, create_token, verify_token, ExpiredSignatureError
# Install: pip install PyJWT
# Run:     python ch08_13_jwt_tokens.py

import jwt
import datetime

SECRET = "key123"    # use a long random string in production

def create_token(user):
    payload = {
        "user": user,
        "exp": datetime.datetime.now(datetime.timezone.utc)
               + datetime.timedelta(hours=1)    # token expires in 1 hour
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None    # token has expired
    except jwt.InvalidTokenError:
        return None    # token is malformed or tampered with

# --- Demo ---
token = create_token("Alice")
print("Token:", token)

payload = verify_token(token)
print("Decoded payload:", payload)   # {'user': 'Alice', 'exp': ...}

# Verify an invalid token
bad = verify_token("this.is.not.valid")
print("Invalid token result:", bad)  # None
