from pydantic import BaseModel

class ScrapeInput(BaseModel):
    url: str
    raw_text: str
