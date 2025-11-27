# Autonomous Procurement Agent
*A multi-agent AI system for supplier discovery, website scraping, structured data extraction, and supplier ranking.*

---

## 🌍 Overview
The Autonomous Procurement Agent is an AI-driven system designed to automate the early stages of procurement: searching for suppliers, extracting structured information from websites, and generating prioritised supplier shortlists.

This project combines:
- Multi-agent architecture  
- Web scraping  
- NLP-based extraction  
- Supplier scoring models  
- LLM reasoning  
- Vector search  

It is part of a 3-project AI portfolio demonstrating innovation in procurement automation (UK Global Talent technical track).

---

## 🎯 Problem Statement
Procurement teams often spend hours:
- Searching for suppliers  
- Scraping websites manually  
- Extracting product specs  
- Comparing pricing, compliance, and fit  

This process is slow, unstructured, and inconsistent.

**AI can automate 60–80% of this process.**

---

## 🚀 Solution
This project creates an **AI procurement assistant** that:
- Reads a requirement  
- Searches for relevant suppliers  
- Scrapes selected websites  
- Extracts structured information  
- Evaluates and ranks suppliers  
- Returns a clear shortlist with reasoning  

This system reduces manual effort and provides a consistent, data-driven process.

---

## 🧩 Key Features

### ✔ Requirement Interpreter
Understands user procurement needs, specifications, constraints.

### ✔ Supplier Search Agent
Searches the web using APIs and semantic expansion.

### ✔ Scraper Agent
Scrapes supplier pages using Playwright/Puppeteer.

### ✔ Information Extraction Agent
Transforms raw HTML/text into structured JSON.

### ✔ Ranking Engine
Evaluates suppliers using configurable scoring models.

### ✔ Orchestrator
Coordinates workflow using CrewAI / AutoGen / LangGraph.

### ✔ Logging & Traceability
Full run logs captured for debugging & audit.

---

## 🏗 Architecture

### High-Level Architecture  
Image stored at:

### Mermaid Diagram

---

## 🧠 Technical Stack

| Layer       | Technology                       |
|-------------|-----------------------------------|
| Frontend    | React (planned)                   |
| Backend     | FastAPI / Python                  |
| Agents      | CrewAI / AutoGen / LangGraph      |
| LLMs        | OpenAI / Anthropic                |
| Scraping    | Playwright / Puppeteer            |
| Vector DB   | Supabase / Pinecone               |
| Logging     | PostgreSQL / JSON logs            |

---

## 🔬 Research Notes
Technical design and analysis documented in:

---

## 🛠 Installation (Coming Soon)
Additional setup steps will be added as the backend evolves.

---

## 📅 Roadmap

### Phase 1 — Core Agents
- [x] Architecture design  
- [x] Research notes  
- [ ] Requirement Interpreter v1  
- [ ] Supplier Search Agent  
- [ ] Scraper Agent  
- [ ] Extraction Agent  
- [ ] Ranking Engine  

### Phase 2 — Orchestration
- [ ] LangGraph pipeline  
- [ ] Error handling & retries  
- [ ] Logging  

### Phase 3 — Frontend
- [ ] React UI  
- [ ] Procurement workflow dashboard  

### Phase 4 — Deployment
- [ ] Docker  
- [ ] Cloud hosting (Render / Vercel / GCP)  


---

## 📜 License
MIT License.
