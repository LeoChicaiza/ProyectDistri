
from fastapi import FastAPI
from app.routes import calculation

app = FastAPI()

app.include_router(calculation.router, prefix="/calculate", tags=["Rate Calculation"])
