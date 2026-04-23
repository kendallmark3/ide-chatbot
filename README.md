# Intent-Driven Engineering Chatbot

A full-stack AI chatbot that answers questions about Intent-Driven Engineering, built with React + FastAPI + Anthropic Claude.

---

## How It Works

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        Browser (User)                           │
│                   http://localhost:5173                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │  User types a message → hits Enter
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   React Frontend (Vite)                         │
│                                                                 │
│   App.jsx          → manages chat state + send logic            │
│   ChatWindow.jsx   → renders message bubbles                    │
│   styles.css       → L'Oreal-inspired minimal theme             │
│                                                                 │
│   POST /chat  ──────────────────────────────────────────────►  │
└──────────────────────────┬──────────────────────────────────────┘
                           │  Vite dev proxy forwards /chat
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  FastAPI Backend (Python)                       │
│                   http://localhost:8000                         │
│                                                                 │
│   POST /chat                                                    │
│     1. Validate request (Pydantic)                              │
│     2. Call Anthropic API  ──────────────────────────────────►  │
│     3. Run enrichment layer                                     │
│     4. Return { answer, references }                            │
│                                                                 │
│   GET /health  → verify API key + live Claude ping              │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Anthropic Claude API                          │
│             model: claude-haiku-4-5-20251001                    │
│             max_tokens: 500                                     │
│             system: Intent-Driven Engineering expert prompt     │
└─────────────────────────────────────────────────────────────────┘
```

---

### Request Lifecycle

```
User types message
       │
       ▼
App.jsx → fetch POST /chat
       │
       │  (Vite proxy)
       ▼
FastAPI /chat endpoint
       │
       ├─► anthropic_client.py
       │       └─► Claude API → returns answer text
       │
       └─► enrichment.py
               └─► scans message + answer for keywords
                   └─► appends matching reference links
       │
       ▼
{ "answer": "...", "references": [...] }
       │
       ▼
React renders bubble + clickable links below response
```

---

### Enrichment Layer

The enrichment layer scans both the user message and Claude's response for keywords and appends curated reference links automatically:

| Keyword detected | Reference added |
|---|---|
| `intent` | LearnTeachMaster.org |
| `anthropic` | docs.anthropic.com |
| `fastapi` | fastapi.tiangolo.com |
| `react` | react.dev |

---

### File Structure

```
bot/
├── backend/
│   ├── main.py                   # FastAPI app, /chat and /health routes
│   ├── services/
│   │   ├── anthropic_client.py   # Claude API wrapper
│   │   └── enrichment.py        # keyword → reference link mapper
│   ├── requirements.txt
│   └── .env                     # ANTHROPIC_API_KEY (gitignored)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # chat state, send logic
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx    # message list renderer
│   │   │   └── MessageBubble.jsx # individual bubble + references
│   │   └── styles.css
│   ├── vite.config.js            # proxies /chat → localhost:8000
│   └── package.json
│
└── .vscode/
    └── settings.json             # enables .env injection in terminals
```

---

## Running Locally

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # add your ANTHROPIC_API_KEY
uvicorn main:app --reload
```

Backend runs at **http://localhost:8000**

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at **http://localhost:5173**

### 3. Verify API key

Open **http://localhost:8000/health** — you should see:

```json
{
  "status": "ok",
  "api_key": "sk-ant-api03...xxxx",
  "test_response": "API key works"
}
```

---

## Recommended Next Steps

### Immediate improvements

- [ ] **Persist chat history** — store conversations in `localStorage` so the session survives a page refresh
- [ ] **Streaming responses** — use Anthropic's streaming API + SSE so the answer types out word-by-word instead of appearing all at once
- [ ] **Error UI** — show a styled error state instead of plain text when the backend is unreachable

### Quality & reliability

- [ ] **Input validation** — enforce max message length on both frontend and backend
- [ ] **Rate limiting** — add `slowapi` middleware to the FastAPI backend to prevent API key exhaustion
- [ ] **Automated tests** — add `pytest` tests for `/chat` and `/health` using `httpx` and a mocked Anthropic client

### Features

- [ ] **Conversation context** — pass the full message history to Claude instead of a single message so it can answer follow-up questions coherently
- [ ] **Expand enrichment keywords** — add more keyword → link mappings (e.g. `claude`, `vite`, `pydantic`)
- [ ] **Export transcript** — let users download the chat as a `.txt` or `.pdf`

### Production readiness

- [ ] **Environment-aware CORS** — replace `allow_origins=["*"]` with the specific frontend domain in production
- [ ] **Docker Compose** — single `docker compose up` to start both services
- [ ] **Deploy** — backend to AWS Fargate or Railway; frontend to Vercel or Netlify
