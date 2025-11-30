from fastapi import APIRouter
from ..models.requirement import RequirementInput

router = APIRouter()

@router.post("/")
def search_suppliers(requirement: RequirementInput):
    """
    Placeholder endpoint for supplier search.
    Week 2 will integrate Tavily / web search APIs.
    """
    return {
        "status": "ok",
        "message": "Search agent placeholder",
        "received_requirement": requirement.dict()
    }
