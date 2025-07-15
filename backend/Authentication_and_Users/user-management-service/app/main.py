
from fastapi import FastAPI
from app.routes import users
from app.database import db

app = FastAPI()



app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}