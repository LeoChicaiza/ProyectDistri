
from fastapi import APIRouter, HTTPException
from app.schemas.ticket import TicketRequest, TicketResponse
from app.database.db import ticket_db

router = APIRouter()

@router.post("/", response_model=TicketResponse)
def issue_ticket(data: TicketRequest):
    if data.ticket_id in ticket_db:
        raise HTTPException(status_code=400, detail="Ticket ID already exists")
    ticket_db[data.ticket_id] = data.dict()
    return TicketResponse(**data.dict())

@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: str):
    ticket = ticket_db.get(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return TicketResponse(**ticket)
