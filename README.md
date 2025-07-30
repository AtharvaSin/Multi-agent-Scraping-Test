# Multi-Agent Scraping Scaffold

This repository provides a minimal scaffold for a multi-agent web scraping
solution with a Python backend and React frontend.

## Backend

The backend lives in the `backend/` directory and contains simple agents:

- **controller.py** – orchestrates the workflow
- **nlp_agent.py** – parses natural language instructions
- **site_analyzer.py** – checks `robots.txt` and determines URLs
- **scraper.py** – fetches pages and extracts data
- **data_normalizer.py** – cleans scraped data
- **storage_manager.py** – stores items in a SQLite database
- **main.py** – FastAPI server exposing a `/run_job` endpoint

Install dependencies and run the API (CORS middleware is enabled by default):

```bash
pip install fastapi uvicorn requests beautifulsoup4
uvicorn backend.main:app --reload
```

## Frontend

A minimal React interface is provided in the `frontend/` directory.
The app is bundled with `esbuild` before serving so the browser can
load the React modules:

```bash
cd frontend
npm install
npm start
```

The frontend posts the user's prompt to the backend and displays how many
items were scraped.

## Usage

1. Start the backend API.
2. Serve the frontend.
3. Enter a natural-language instruction in the textarea and run the job.

This scaffold is intentionally lightweight so you can extend each agent as
needed for your project.
