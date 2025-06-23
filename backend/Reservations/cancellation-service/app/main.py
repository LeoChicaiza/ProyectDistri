
from fastapi import FastAPI
from app.routes import cancellation
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(cancellation.router, prefix="/cancellations", tags=["Cancellations"])
