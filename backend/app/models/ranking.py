from pydantic import BaseModel
from typing import List, Dict, Any

class RankingInput(BaseModel):
    suppliers: List[Dict[str, Any]]
    requirement: Dict[str, Any]
