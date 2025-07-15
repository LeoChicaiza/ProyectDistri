from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.user import UserLogin, TokenResponse, UserOut
from app.utils.jwt_handler import create_jwt_token, verify_jwt_token
from app.database.db import get_connection
import psycopg2.extras
import bcrypt
import requests



router = APIRouter(prefix="/auth", tags=["Auth"])
security = HTTPBearer()

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(
        "SELECT user_id, email, password_hash, role, is_active FROM users WHERE email = %s",
        (user.email,),
    )
    db_user = cur.fetchone()
    conn.close()

    if not db_user:
        raise HTTPException(401, "Credenciales inválidas")
    if not db_user["is_active"]:
        raise HTTPException(403, "Cuenta inactiva")
    if not bcrypt.checkpw(user.password.encode(), db_user["password_hash"].encode()):
        raise HTTPException(401, "Contraseña incorrecta")
    
    if not bcrypt.checkpw(
        user.password.encode(),
        db_user["password_hash"].encode()
    ):
       # Llamada a login-audit-service en fallo
        requests.post(
            "http://login-audit-service:5000/audit",
            json={"userId": db_user["user_id"], "action": "login", "status": "failure"}
        )
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = create_jwt_token({
        "user_id": db_user["user_id"],
        "email": db_user["email"],
        "role": db_user["role"],
    })
    return TokenResponse(access_token=token)

@router.get("/me", response_model=UserOut)
def me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = verify_jwt_token(credentials.credentials)
    if payload is None:
        raise HTTPException(401, "Token inválido")
    return UserOut(
        user_id=payload["user_id"],
        email=payload["email"],
        role=payload["role"],
    )
