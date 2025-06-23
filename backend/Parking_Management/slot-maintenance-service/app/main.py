
from fastapi import FastAPI
from app.routes import maintenance
from app.database import db

app = FastAPI()



app.include_router(maintenance.router, prefix="/maintenance", tags=["Slot Maintenance"])
