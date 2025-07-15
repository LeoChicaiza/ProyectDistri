
from fastapi import APIRouter, Depends, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel
import httpx
import os

router = APIRouter()

class UserMeResponse(BaseModel):
    user_id: str
    email: str
    role: str
    full_name: str
    phone_number: str

def decode_token(auth_header: str):
    try:
        scheme, token = auth_header.split()
        payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        return payload
    except Exception as e:
        raise HTTPException(401, "Token inválido")

@router.get("/me", response_model=UserMeResponse)
async def get_own_profile(authorization: str = Depends(lambda: None)):
    # 1) Decodifico el JWT
    if not authorization:
        raise HTTPException(401, "Falta cabecera Authorization")
    data = decode_token(authorization)

    # 2) Llamo a user-management-service para obtener perfil
    user_id = data["user_id"]
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://user-management-service:8006/users/{user_id}")
    if resp.status_code != 200:
        raise HTTPException(resp.status_code, f"No pude recuperar perfil: {resp.text}")

    profile = resp.json()
    return UserMeResponse(
        user_id=user_id,
        email=data["email"],
        role=data["role"],
        full_name=profile["full_name"],
        phone_number=profile["phone_number"],
    )
