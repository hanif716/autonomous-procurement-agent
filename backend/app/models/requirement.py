from pydantic import BaseModel
from typing import List, Optional

class RequirementInput(BaseModel):
    category: str
    product: str
    location: str
    quantity: int
    required_certifications: Optional[List[str]] = None
