# Autonomous Procurement Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge" />
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Agent%20Systems-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenAI-API-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## Overview

The **Autonomous Procurement Agent** is an AI-driven, multi-agent system designed to automate:

- Supplier discovery  
- Website scraping  
- Structured information extraction  
- Supplier scoring and ranking  
- Predictive comparison and similarity search  
- Dashboard visualisation (React)  

This project combines:

- Multi-agent orchestration  
- Web scraping & extraction  
- LLM-powered analysis  
- Vector search (FAISS/Chroma)  
- FastAPI + React architecture  

---

## 🚀 Quick Start

This guide helps you run the Autonomous Procurement Agent **locally** for development and testing.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hanif716/autonomous-procurement-agent.git
cd autonomous-procurement-agent
2️⃣ Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
3️⃣ Install Backend Dependencies
bash
Copy code
pip install -r backend/app/requirements.txt
4️⃣ Run the Backend (FastAPI)
bash
Copy code
uvicorn app.main:app --reload --app-dir backend/app
Open the API docs:

👉 http://127.0.0.1:8000/docs

You should see endpoints for:

Supplier search

Extraction

Ranking

Root health check

🛠️ Tech Stack
Backend
Python 3.10+

FastAPI

Pydantic

Uvicorn

LangChain Tools

FAISS / Chroma

Frontend
React

TailwindCSS

Chart.js / Recharts

AI Components
OpenAI models

Embedding models (text-embedding-3-large)

Tool-based agent workflows

🧱 Architecture
A full system design diagram is available at:

📄 docs/architecture.png

🗺 Roadmap
Phase 1 – Backend
 FastAPI skeleton

 Supplier scraping module

 Extraction agent

 Ranking model

Phase 2 – Agents
 Supervisor agent

 Search agent

 Extraction agent

 Ranking agent

Phase 3 – Frontend
 React UI

 Supplier dashboard

 Ranking analytics

Phase 4 – Deployment
 Docker

 Cloud hosting (Render / Vercel / GCP)

📄 License
MIT License.