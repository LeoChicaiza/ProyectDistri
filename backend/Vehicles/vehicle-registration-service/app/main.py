from fastapi import FastAPI
from app.routes import vehicles

app = FastAPI()

app.include_router(vehicles.router, prefix="/vehicles", tags=["Vehicles"])

