
from fastapi import FastAPI
from app.routes import ticket
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(ticket.router, prefix="/tickets", tags=["Ticket Management"])
