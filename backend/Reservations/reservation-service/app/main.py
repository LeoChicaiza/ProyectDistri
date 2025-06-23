
from fastapi import FastAPI
from app.routes import reservation
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(reservation.router, prefix="/reservations", tags=["Reservations"])
