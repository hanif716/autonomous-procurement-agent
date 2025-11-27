# Roadmap – Autonomous Procurement Agent

## Phase 1 — Foundations
- [x] Project structure created
- [x] Architecture diagram added
- [x] Research notes completed
- [ ] Define data models (supplier, requirements, ranking)
- [ ] Create `.env.example` and config templates

## Phase 2 — Core Agent Development
- [ ] Requirement Interpreter (LLM prompt + schema)
- [ ] Supplier Search Agent (Tavily / API search)
- [ ] Scraper Agent (Playwright or Puppeteer)
- [ ] Information Extraction Agent (structured JSON)
- [ ] Ranking Engine (scoring system)
- [ ] Orchestrator (CrewAI / LangGraph / AutoGen version)

## Phase 3 — Backend API (FastAPI)
- [ ] Implement `/search` endpoint
- [ ] Implement `/scrape` endpoint
- [ ] Implement `/rank` endpoint
- [ ] Add logging + error handling
- [ ] Add request validation

## Phase 4 — Data & Storage
- [ ] Save supplier profiles to database
- [ ] Add caching layer for repeated searches
- [ ] Add job queue (optional)

## Phase 5 — Frontend
- [ ] Basic React dashboard
- [ ] View suppliers
- [ ] View ranking scores
- [ ] Trigger agent pipeline

## Phase 6 — Testing & Quality
- [ ] Unit tests for extraction
- [ ] Integration tests for pipeline
- [ ] Example input + example output JSON

## Phase 7 — Deployment
- [ ] Dockerfile + Docker Compose
- [ ] Deploy API to Render / Railway / GCP
- [ ] Deploy frontend to Vercel

