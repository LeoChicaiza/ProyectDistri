import jwt
from datetime import datetime, timedelta
import os
from jwt import PyJWTError

SECRET_KEY = os.getenv("JWT_SECRET", "secreto123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 1

def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        return None


