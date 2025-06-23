
from fastapi import FastAPI
from app.routes import billing
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(billing.router, prefix="/billing", tags=["Billing and Payment"])
