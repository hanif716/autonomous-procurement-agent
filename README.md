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

The **Autonomous Procurement Agent** is an AI-powered multi-agent system that automates:

- Supplier discovery  
- Website scraping  
- Structured information extraction  
- Supplier scoring and ranking  
- Predictive comparison and similarity search  
- Dashboard visualisation (React)

### Key Features

- Multi-agent orchestration  
- Web scraping & extraction  
- LLM-powered analysis  
- Vector search (FAISS / Chroma)  
- FastAPI backend + React frontend  

---

## 🚀 Quick Start

Follow these steps to run the project locally.

---

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/hanif716/autonomous-procurement-agent.git
cd autonomous-procurement-agent
```

---

### **2️⃣ Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

---

### **3️⃣ Install Backend Dependencies**

```bash
pip install -r backend/app/requirements.txt
```

---

### **4️⃣ Run the Backend (FastAPI)**

```bash
uvicorn app.main:app --reload --app-dir backend/app
```

Now open the API docs:

👉 **http://127.0.0.1:8000/docs**

You will see endpoints for:

- Supplier search (`/search`)
- Extraction (`/extract`)
- Ranking (`/rank`)
- Root health check (`/`)

---

## 🛠️ Tech Stack

### **Backend**
- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- LangChain tools
- FAISS / Chroma vector DB

### **Frontend**
- React  
- TailwindCSS  
- Recharts / Chart.js  

### **AI Components**
- OpenAI models  
- Embeddings (`text-embedding-3-large`)  
- Tool-based agent workflows  

---

## 🧱 Architecture

A full architecture diagram is included:

📄 `docs/architecture.png`

---

## 🗺 Roadmap

### **Phase 1 – Backend**
- [ ] FastAPI skeleton  
- [ ] Supplier scraping module  
- [ ] Extraction agent  
- [ ] Ranking model  

### **Phase 2 – Agents**
- [ ] Supervisor agent  
- [ ] Search agent  
- [ ] Extraction agent  
- [ ] Ranking agent  

### **Phase 3 – Frontend**
- [ ] React UI  
- [ ] Supplier dashboard  
- [ ] Ranking analytics  

### **Phase 4 – Deployment**
- [ ] Docker  
- [ ] Cloud hosting (Render / Vercel / GCP)

---

## 📄 License

MIT License.
