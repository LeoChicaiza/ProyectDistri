
from fastapi import FastAPI
from app.routes import sessions
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(sessions.router, prefix="/sessions", tags=["Active Sessions"])
