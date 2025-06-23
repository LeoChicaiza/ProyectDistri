from fastapi import APIRouter, HTTPException
from app.schemas.session import SessionCreate, SessionResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/start", response_model=SessionResponse)
def start_session(data: SessionCreate):
    conn = get_connection()
    cur = conn.cursor()
    session_id = str(uuid.uuid4())
    try:
        cur.execute("""
            INSERT INTO active_sessions (session_id, user_id, ip_address, user_agent)
            VALUES (%s, %s, %s, %s)
            RETURNING session_id, user_id, ip_address, user_agent, login_time, is_active
        """, (session_id, data.user_id, data.ip_address, data.user_agent))
        result = cur.fetchone()
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return SessionResponse(
        session_id=result[0],
        user_id=result[1],
        ip_address=result[2],
        user_agent=result[3],
        login_time=result[4],
        is_active=result[5]
    )

@router.get("/user/{user_id}", response_model=list[SessionResponse])
def get_active_sessions(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT session_id, user_id, ip_address, user_agent, login_time, is_active
            FROM active_sessions
            WHERE user_id = %s AND is_active = TRUE
        """, (user_id,))
        rows = cur.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return [
        SessionResponse(
            session_id=row[0],
            user_id=row[1],
            ip_address=row[2],
            user_agent=row[3],
            login_time=row[4],
            is_active=row[5]
        ) for row in rows
    ]

@router.post("/end/{session_id}")
def end_session(session_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE active_sessions
            SET is_active = FALSE
            WHERE session_id = %s
        """, (session_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Session not found")
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"message": f"Session {session_id} closed successfully"}


