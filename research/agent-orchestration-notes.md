# Autonomous Procurement Agent – Technical Research Notes  
**Project:** Autonomous Procurement Agent  
**Author:** Hanif Hazrati  

---

## 1. Purpose of the Autonomous Procurement Agent

Procurement teams spend significant time:

- searching the web for suppliers  
- manually reviewing supplier websites  
- extracting product info  
- checking compliance  
- comparing vendors  
- building shortlists  

These tasks are slow, repetitive, and inconsistent.

The Autonomous Procurement Agent aims to:

- ✔ Automate supplier discovery  
- ✔ Automate website scraping  
- ✔ Extract structured product data  
- ✔ Evaluate vendors using scoring models  
- ✔ Produce a ranked shortlist  
- ✔ Reduce manual procurement workload  

This project showcases innovation in procurement automation — incredibly relevant for UK Global Talent.

---

## 2. Multi-Agent Architecture Overview

The system uses multiple coordinated agents:

1. **Requirement Interpreter Agent**  
   Parses user needs and converts them into structured specifications.

2. **Supplier Search Agent**  
   Performs semantic web search using APIs (Google, Bing, Tavily).

3. **Scraper Agent**  
   Fetches and processes supplier websites using headless browsers.

4. **Information Extraction Agent**  
   Uses LLMs to extract product/service details into clean JSON.

5. **Ranking Agent**  
   Scores vendors based on requirement fit, compliance, and capability.

6. **Orchestrator Agent**  
   Controls the workflow and manages agent-to-agent communication.

### Architecture Summary Table

| Agent                        | Purpose                                  |
|-----------------------------|-------------------------------------------|
| Requirement Interpreter     | Structure procurement needs               |
| Supplier Search             | Find relevant vendors                     |
| Scraper                     | Extract raw website content               |
| Information Extraction      | Convert content → structured data         |
| Ranking                     | Score suppliers                           |
| Orchestrator                | Manage workflow + state                   |

---

## 3. Requirement Interpreter — Technical Notes

This agent converts plain English requirements into structured variables.

Example input:

> “We need a catering supplier in Manchester for 100 guests.”

Structured output:

<div style="background:#f6f8fa; padding:10px; border-radius:8px;">
<pre>
{
  "category": "catering",
  "location": "Manchester, UK",
  "quantity": 100,
  "requirements": ["event catering", "food", "service staff"]
}
</pre>
</div>

Techniques:

- entity extraction  
- semantic parsing  
- normalisation rules  
- template-based mapping  

---

## 4. Supplier Search Agent — Technical Process

The search agent:

- expands keywords  
- performs semantic search  
- queries APIs  
- filters irrelevant links  
- produces ranked URLs  

Example output:

<div style="background:#f6f8fa; padding:10px; border-radius:8px;">
<pre>
[
  {"url": "https://supplier1.com", "relevance": 0.92},
  {"url": "https://supplier2.com", "relevance": 0.85}
]
</pre>
</div>

Uses:

- Tavily API  
- custom relevance scoring  
- LLM-enhanced search term expansion  

---

## 5. Scraper Agent — Technical Notes

Responsibilities:

- load pages using headless browser (Playwright/Puppeteer)  
- handle dynamic JS pages  
- scroll & wait for data  
- extract visible text + metadata  

Example raw output:

<div style="background:#f6f8fa; padding:10px; border-radius:8px;">
<pre>
{
  "url": "https://supplier1.com",
  "raw_text": "...",
  "metadata": {"title": "Supplier 1"}
}
</pre>
</div>

---

## 6. Information Extraction Agent

This agent uses LLMs to extract structured information from raw text.

Tasks include:

- extracting products  
- extracting pricing clues  
- identifying certifications  
- detecting company capability  
- finding contact details  

Example structured output:

<div style="background:#f6f8fa; padding:10px; border-radius:8px;">
<pre>
{
  "company": "Supplier 1",
  "products": ["Infusion Pump", "ECG Machine"],
  "certifications": ["ISO 9001"],
  "contact_email": "info@supplier1.com"
}
</pre>
</div>

---

## 7. Vendor Ranking Engine — Scoring Logic

Factors:

- requirement match  
- product/capability fit  
- geographic fit  
- compliance signals  
- credibility indicators  

Example pseudo-scoring algorithm:

<div style="background:#f6f8fa; padding:10px; border-radius:8px;">
<pre>
score = (fit_score * 0.4) +
        (compliance * 0.3) +
        (credibility * 0.2) +
        (location_match * 0.1)
</pre>
</div>

Outputs:

- ranked list  
- justification text  
- structured scoring breakdown  

---

## 8. Orchestrator Logic

Controls:

- workflow order  
- state  
- retries  
- error handling  
- passing data between agents  

Example orchestration flow:

<div style="background:#f6f8fa; padding:10px; border-radius:8px;">
<pre>
User Requirement
    ↓
Interpreter Agent
    ↓
Search Agent
    ↓
Scraper Agent
    ↓
Extraction Agent
    ↓
Ranking Agent
    ↓
Final Shortlist Output
</pre>
</div>

---

## 9. Example End-to-End Output

<div style="background:#f6f8fa; padding:10px; border-radius:8px;">
<pre>
{
  "top_suppliers": [
    {
      "name": "Supplier A",
      "score": 0.91,
      "reason": "Strong match on category and compliance"
    },
    {
      "name": "Supplier B",
      "score": 0.84,
      "reason": "Good capability but weaker documentation"
    }
  ]
}
</pre>
</div>

---

