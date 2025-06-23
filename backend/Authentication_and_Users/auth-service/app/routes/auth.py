from fastapi import APIRouter, HTTPException
from app.schemas.user import UserLogin, TokenResponse
from app.utils.jwt_handler import create_jwt_token
from app.database.db import get_connection
import psycopg2.extras
import bcrypt

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("SELECT user_id, email, password_hash, role, is_active FROM users WHERE email = %s", (user.email,))
    db_user = cursor.fetchone()

    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    if not db_user["is_active"]:
        raise HTTPException(status_code=403, detail="Cuenta inactiva")

    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user["password_hash"].encode('utf-8')):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = create_jwt_token({
        "user_id": db_user["user_id"],
        "email": db_user["email"],
        "role": db_user["role"]
    })

    return TokenResponse(access_token=token)

