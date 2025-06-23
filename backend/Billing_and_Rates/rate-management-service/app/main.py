
from fastapi import FastAPI
from app.routes import rate
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(rate.router, prefix="/rates", tags=["Rate Management"])
