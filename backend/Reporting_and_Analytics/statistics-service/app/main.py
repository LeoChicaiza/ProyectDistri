
from fastapi import FastAPI
from app.routes import stats
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(stats.router, prefix="/stats", tags=["Statistics"])
