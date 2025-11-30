from fastapi import APIRouter
from ..models.scrape import ScrapeInput
from pathlib import Path
import json

router = APIRouter()

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "samples"


@router.post("/")
def extract_information(data: ScrapeInput):
    """
    MVP logic:
    - Loads sample_extracted_supplier.json
    - Returns structured supplier data
    """

    sample_file = DATA_DIR / "sample_extracted_supplier.json"

    with open(sample_file, "r") as f:
        sample_output = json.load(f)

    return {
        "status": "success",
        "supplier_extracted": sample_output,
        "source_url": data.url
    }
