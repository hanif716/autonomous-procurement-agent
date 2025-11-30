from fastapi import APIRouter
from ..models.ranking import RankingInput

router = APIRouter()

@router.post("/")
def rank_suppliers(data: RankingInput):
    """
    Placeholder for vendor ranking.
    Week 2 will integrate scoring algorithms.
    """
    return {
        "status": "ok",
        "message": "Ranking agent placeholder",
        "received_data": data.dict()
    }
