from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str

class UserOut(BaseModel):
    user_id: str
    email: EmailStr
    role: str


