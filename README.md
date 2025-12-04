# Multi-Agent Research Assistant

A powerful research assistant powered by LangChain, Groq, and Streamlit.

## 🚀 Live Demo
[**Try the App Here**](https://multi-agent-research-assistant-kb6eu2xhmx5bhizdrbrvwd.streamlit.app/)

## Features
- **Planner Agent**: Breaks down queries into sub-tasks.
- **Search Agent**: Scrapes the web for information.
- **Retriever Agent**: Uses RAG to find relevant context.
- **Critic Agent**: Validates answers and removes hallucinations.
- **Writer Agent**: Generates structured reports.
- **Streamlit UI**: Easy-to-use interface.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   Copy `.env.example` to `.env` and add your Groq API Key.
   ```bash
   cp .env.example .env
   ```

3. **Run the App**:
   ```bash
   streamlit run app/streamlit_app.py
   ```

## Architecture
User Query -> Planner -> Subtasks -> Search -> RAG -> Critic -> Writer -> Report
