from fastapi import FastAPI
from app.routes import access
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    
    connection = db.get_connection()
    connection.close()  


app.include_router(access.router, prefix="/access", tags=["Access Control"])
