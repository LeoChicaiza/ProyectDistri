
from fastapi import FastAPI
from app.routes import parkings
from app.database import db

app = FastAPI()



app.include_router(parkings.router, prefix="/parking-lots", tags=["Parking Lots"])
