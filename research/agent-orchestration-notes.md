Agent Orchestration – Technical Research Notes

Project: Autonomous Procurement Agent
Author: Hanif Hazrati

🧠 1. Overview of Multi-Agent AI Systems

Multi-agent systems involve multiple specialised AI components (agents) that work together to perform a task that is too complex for a single LLM call.

In procurement automation, this approach is useful because:

Supplier search

Web scraping

Information extraction

Risk/score analysis

Decision-making

are all different cognitive tasks, best handled by separate agents.

This improves performance, accuracy, explainability, and traceability.

🤖 2. Why Use Agent Orchestration in Procurement

Traditional procurement workflows are:

Manual

Time-consuming

Error-prone

Non-standardised

Multi-agent AI automates these steps:

Understanding the requirement

Finding suppliers

Scraping websites

Extracting structured details

Ranking suppliers

Producing a final recommendation

This system creates an automated “procurement assistant” that reduces work hours and improves quality.

🔀 3. Key Components of an Agent System
3.1 Orchestrator

The orchestrator coordinates the workflow:

Routes tasks to specific agents

Manages memory

Tracks task failures

Controls the sequence of actions

Collects final outputs

Framework options:

CrewAI

AutoGen

LangGraph (LangChain)

👤 3.2 Requirement Interpreter Agent

Purpose:
Convert a user requirement into a structured procurement query.

Skills:

NLP interpretation

Constraint detection (budget, quantity)

Category classification

Data normalisation

Example prompt snippet:

“Extract user intent, category, budget, quantity, technical specifications, mandatory features…”

🔍 3.3 Supplier Search Agent

Purpose:
Find suppliers online using search APIs or custom queries.

Techniques:

Web search APIs

Google Custom Search

Semantic search

Keyword expansion

Outputs:

Supplier names

Website URLs

Contact info (if available)

🌐 3.4 Web Scraper Agent

Purpose:
Scrape supplier websites for relevant products/services.

Tools:

Playwright

Puppeteer

BeautifulSoup

Extracts:

Product names

Technical descriptions

Pricing

Lead time

Compliance info

🧾 3.5 Information Extraction Agent

Purpose:
Convert scraped HTML or text into structured JSON.

Techniques:

LLM text parsing

Regular expressions

Keyword detection

Embedding-based similarity

Outputs:

{
  "product": "",
  "specs": "",
  "price": "",
  "compliance": "",
  "contact": "",
  "url": ""
}

⭐ 3.6 Ranking and Scoring Agent

Purpose:
Evaluate suppliers based on quality, price, compliance, and availability.

Ranking model can include:

Weighted scoring

Semantic evaluation

Cost comparison

Risk and reliability indicators

This agent produces final supplier recommendations.

💾 4. Memory & Logging

Every step logs:

Agent inputs

Agent outputs

Errors

LLM token usage

Cost

Execution time

This provides:

Traceability

Debugging capability

Evidence for the final report

Training dataset for optimisation

🧩 5. End-to-End Workflow

User enters procurement requirement

Orchestrator activates Requirement Interpreter Agent

Supplier Search Agent finds potential suppliers

Scraper Agent fetches website pages

Extraction Agent parses structured data

Ranking Agent evaluates suppliers

Backend returns JSON to frontend

Dashboard shows ranked list

🧠 6. Example Orchestrator Logic (Pseudocode)
def run_procurement_pipeline(requirement):
    interpreted = requirement_agent.run(requirement)
    suppliers = search_agent.find(interpreted)
    pages = scraper_agent.scrape(suppliers)
    extracted = extraction_agent.process(pages)
    ranked = ranking_agent.score(extracted, interpreted)
    return ranked

🔧 7. Technical Tools Used
LLM Providers

OpenAI GPT-4.1

Anthropic Claude 3.5

Agent Frameworks

CrewAI

LangGraph

AutoGen

Scraping

Playwright

Puppeteer

Embedding Databases

Supabase Vector DB

Pinecone

Chroma