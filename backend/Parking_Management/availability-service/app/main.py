
from fastapi import FastAPI
from app.routes import availability
from app.database import db

app = FastAPI()

app.include_router(availability.router, prefix="/availability", tags=["Availability"])

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}