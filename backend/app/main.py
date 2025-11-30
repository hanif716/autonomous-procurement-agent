from fastapi import FastAPI
from .routers import search, extract, rank

app = FastAPI(
    title="Autonomous Procurement Agent API",
    description="Backend API for supplier search, extraction, and ranking.",
    version="0.1.0"
)

# Register routers
app.include_router(search.router, prefix="/search", tags=["Search"])
app.include_router(extract.router, prefix="/extract", tags=["Extraction"])
app.include_router(rank.router, prefix="/rank", tags=["Ranking"])


@app.get("/")
def root():
    return {"message": "Autonomous Procurement Agent backend is running."}
