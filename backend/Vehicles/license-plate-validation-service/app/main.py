
from fastapi import FastAPI
from app.routes import validate

app = FastAPI()

app.include_router(validate.router, prefix="/plate-validation", tags=["Plate Validation"])
