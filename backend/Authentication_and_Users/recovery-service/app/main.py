
from fastapi import FastAPI
from app.routes import recovery
from app.database import db

app = FastAPI()


app.include_router(recovery.router, prefix="/recovery", tags=["Password Recovery"])

@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}