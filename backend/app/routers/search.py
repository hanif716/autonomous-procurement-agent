from fastapi import APIRouter
from ..models.requirement import RequirementInput
from pathlib import Path
import json

router = APIRouter()

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "samples"


@router.post("/")
def search_suppliers(requirement: RequirementInput):
    """
    MVP logic:
    - Load sample search results from JSON
    - Simulate a basic relevance filter
    """

    sample_file = DATA_DIR / "sample_search_results.json"

    with open(sample_file, "r") as f:
        results = json.load(f)

    # Basic simulation: boost relevance if product keyword matches
    filtered_results = []
    for item in results:
        score = item["relevance"]
        if requirement.product.lower() in item["url"].lower():
            score += 0.05

        filtered_results.append({
            "url": item["url"],
            "relevance": round(score, 3)
        })

    return {
        "status": "success",
        "query": requirement.dict(),
        "results": filtered_results
    }
