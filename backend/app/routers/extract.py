from fastapi import APIRouter
from ..models.scrape import ScrapeInput

router = APIRouter()

@router.post("/")
def extract_information(data: ScrapeInput):
    """
    Placeholder endpoint for extraction agent.
    Week 2 will integrate LLM-based extraction.
    """
    return {
        "status": "ok",
        "message": "Extraction agent placeholder",
        "received_data": data.dict()
    }
