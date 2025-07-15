
from fastapi import FastAPI
from app.routes import zones
from app.database import db

app = FastAPI()



app.include_router(zones.router, prefix="/zones", tags=["Zones"])

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}