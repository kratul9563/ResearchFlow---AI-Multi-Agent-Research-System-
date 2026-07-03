# ResearchFlow AI: Multi-Agent Research Intelligence System

ResearchFlow AI is an Agentic AI application built using LangChain and Large Language Models (LLMs) that automates the complete research workflow through multiple specialized AI agents. The system performs web search, content extraction, report generation, and quality evaluation by orchestrating collaborative AI agents in a sequential pipeline.

## Features

* Multi-Agent AI architecture using LangChain
* Automated web search using Tavily Search API
* Intelligent web content scraping and extraction
* AI-powered research report generation
* Automated report evaluation using Critic Agents
* End-to-end agent orchestration and state management
* Interactive Streamlit-based user interface

## System Architecture

The system consists of four specialized AI agents:

* **Search Agent** – Retrieves recent and reliable information from the web
* **Reader Agent** – Scrapes and extracts detailed content from selected sources
* **Writer Agent** – Generates structured and professional research reports
* **Critic Agent** – Reviews and evaluates the quality of generated reports

## Tech Stack

* Python
* LangChain
* Large Language Models (OpenAI/Gemini/Groq)
* Tavily Search API
* BeautifulSoup
* Streamlit
* Requests
* Pydantic

## Workflow

User Query → Search Agent → Reader Agent → Writer Agent → Critic Agent → Final Research Report

## Key Features

* Agentic AI Workflow
* Multi-Agent Collaboration
* Web Search and Scraping
* Research Automation
* Report Generation
* AI-based Quality Evaluation

## Future Improvements

* Integration with LangGraph
* Memory-enabled agents
* Multi-source validation
* PDF export support
* Human-in-the-loop feedback system
