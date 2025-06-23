from fastapi import APIRouter
from datetime import datetime
from app.database.db import get_connection

router = APIRouter()

@router.post("/log-login")
def log_login(user_id: str, success: bool):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO login_audit (user_id, success, timestamp) VALUES (%s, %s, %s)",
                (user_id, success, datetime.utcnow()))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Login attempt recorded"}
