
from fastapi import FastAPI
from app.routes import history

app = FastAPI()

app.include_router(history.router, prefix="/history", tags=["Vehicle History"])

