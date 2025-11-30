from fastapi import APIRouter
from ..models.ranking import RankingInput

router = APIRouter()


@router.post("/")
def rank_suppliers(data: RankingInput):
    """
    MVP logic:
    Simple scoring:
    - Matching certifications +0.5
    - Product match +0.3
    - Location match +0.2
    """

    requirement = data.requirement
    required_product = requirement.get("product", "").lower()

    final_rankings = []

    for sup in data.suppliers:
        score = 0.0

        # Score based on product match
        if required_product in str(sup.get("products", "")).lower():
            score += 0.3

        # Score based on certifications
        required_certs = requirement.get("required_certifications", [])
        supplier_certs = sup.get("certifications", [])

        matches = len(set(required_certs) & set(supplier_certs))
        score += matches * 0.5

        # Location match
        if requirement.get("location", "").lower() in sup.get("location", "").lower():
            score += 0.2

        final_rankings.append({
            "supplier": sup,
            "score": round(score, 3)
        })

    # Sort by score descending
    final_rankings.sort(key=lambda x: x["score"], reverse=True)

    return {
        "status": "success",
        "ranked_suppliers": final_rankings
    }
