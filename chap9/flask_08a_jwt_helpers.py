# flask_08a_jwt_helpers.py
# Section: JSON Web Tokens - token creation and verification
# Demonstrates: jwt.encode, jwt.decode, expiry, error handling
# Install: pip install PyJWT
# Run: python flask_08a_jwt_helpers.py  (standalone demo)

import jwt
import datetime

SECRET_KEY = "replace-with-a-long-random-secret"


def create_token(user_id: int, username: str) -> str:
    """Create a signed JWT that expires in 1 hour."""
    payload = {
        "sub":      user_id,    # subject (standard JWT claim)
        "username": username,
        "exp":      datetime.datetime.now(datetime.timezone.utc)
                    + datetime.timedelta(hours=1),
        "iat":      datetime.datetime.now(datetime.timezone.utc),
                                # issued at (standard JWT claim)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def verify_token(token: str) -> dict | None:
    """Decode and verify a JWT. Returns the payload dict or None."""
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None    # token has expired
    except jwt.InvalidTokenError:
        return None    # token is malformed or signature is invalid


# ------------------------------------------------------------------
# Standalone demo
# ------------------------------------------------------------------
if __name__ == "__main__":
    token = create_token(1, "alice")
    print("Token:", token)

    payload = verify_token(token)
    print("Decoded:", payload)

    print("Invalid token:", verify_token("this.is.not.valid"))
