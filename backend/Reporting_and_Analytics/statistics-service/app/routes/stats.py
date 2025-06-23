
from fastapi import APIRouter
from app.schemas.stats import StatsResponse
from app.database.db import visit_count

router = APIRouter()

@router.get("/visits", response_model=StatsResponse)
def get_visit_stats():
    visit_count["total"] += 1
    return StatsResponse(message="Stat updated", total_visits=visit_count["total"])
