from fastapi import APIRouter, HTTPException
from uuid import uuid4
from datetime import datetime
from app.schemas.recovery import RecoveryRequestCreate, RecoveryRequestResponse
from app.database.db import get_connection

router = APIRouter()

@router.post("/create", response_model=RecoveryRequestResponse)
def create_recovery_request(request: RecoveryRequestCreate):
    recovery_id = str(uuid4())
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO recovery_requests (recovery_id, user_id, token, expires_at, used)
            VALUES (%s, %s, %s, %s, %s)
        """, (recovery_id, request.user_id, request.token, request.expires_at, False))

        conn.commit()

        return RecoveryRequestResponse(
            recovery_id=recovery_id,
            user_id=request.user_id,
            token=request.token,
            expires_at=request.expires_at,
            used=False,
            requested_at=datetime.utcnow()
        )
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cur.close()
        conn.close()

@router.get("/{user_id}", response_model=list[RecoveryRequestResponse])
def get_requests_by_user(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT recovery_id, user_id, token, expires_at, used, requested_at
            FROM recovery_requests
            WHERE user_id = %s
        """, (user_id,))
        rows = cur.fetchall()
        return [
            RecoveryRequestResponse(
                recovery_id=row[0],
                user_id=row[1],
                token=row[2],
                expires_at=row[3],
                used=row[4],
                requested_at=row[5]
            ) for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cur.close()
        conn.close()


