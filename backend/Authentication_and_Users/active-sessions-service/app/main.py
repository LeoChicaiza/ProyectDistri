
from fastapi import FastAPI
from app.routes import sessions
from app.database import db

app = FastAPI()



app.include_router(sessions.router, prefix="/sessions", tags=["Active Sessions"])

@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}