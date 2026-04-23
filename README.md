# Intent-Driven Engineering Chatbot

A full-stack AI chatbot that answers questions about Intent-Driven Engineering, built with React + FastAPI + Anthropic Claude.

**GitHub:** https://github.com/kendallmark3/ide-chatbot

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
│   MessageBubble.jsx → markdown rendering + token display        │
│   styles.css       → minimal dark-gradient theme                │
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
│     1. Validate request — 1 to 2000 chars (Pydantic)            │
│     2. Call Anthropic API  ──────────────────────────────────►  │
│     3. Run enrichment layer                                     │
│     4. Return { answer, references, usage }                     │
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
       │       └─► Claude API → returns { text, input_tokens, output_tokens }
       │
       └─► enrichment.py
               └─► scans message + answer for keywords
                   └─► appends matching reference links
       │
       ▼
{ "answer": "...", "references": [...], "usage": { input_tokens, output_tokens } }
       │
       ▼
React renders markdown bubble + reference links + token count
```

---

### Enrichment Layer

Scans both the user message and Claude's response for keywords and appends curated reference links automatically:

| Keyword detected | Reference added |
|---|---|
| `intent` | LearnTeachMaster.org |
| `anthropic` | docs.anthropic.com |
| `fastapi` | fastapi.tiangolo.com |
| `react` | react.dev |

---

### Token Usage

Every assistant response displays token counts below the bubble:

```
↑ 142 in · 87 out · 229 total tokens
```

**Cost estimate (claude-haiku-4-5):** ~$0.001 per conversation. 50,000 prompts ≈ $40–50 total.

---

### File Structure

```
bot/
├── backend/
│   ├── main.py                   # FastAPI app — /chat and /health routes
│   ├── services/
│   │   ├── anthropic_client.py   # Claude API wrapper, returns text + token usage
│   │   └── enrichment.py        # keyword → reference link mapper
│   ├── requirements.txt
│   └── .env                     # ANTHROPIC_API_KEY (gitignored)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # chat state, send logic, usage passthrough
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx    # message list renderer
│   │   │   └── MessageBubble.jsx # markdown bubble + references + token count
│   │   └── styles.css            # markdown styles, token badge, bubble theme
│   ├── vite.config.js            # proxies /chat → localhost:8000
│   └── package.json              # react-markdown included
│
├── .vscode/
│   └── settings.json             # python.terminal.useEnvFile enabled
├── intent.md                     # original intent file used to generate this app
└── README.md
```

---

## Running Locally

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # paste your ANTHROPIC_API_KEY
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

```bash
curl http://localhost:8000/health
```

Expected:
```json
{ "status": "ok", "test_response": "API key works" }
```

---

## Security

| Area | Implementation |
|---|---|
| CORS | Locked to `localhost:5173` / `5181`; override via `ALLOWED_ORIGINS` env var |
| Input length | 1–2000 characters enforced via Pydantic `Field` |
| API key | Never exposed in responses; only read server-side from `.env` |
| Error handling | Internal exceptions return `502`, no stack traces leaked |
| Reference URLs | Frontend validates `http/https` only; `rel="noopener noreferrer"` |

---

## Recommended Next Steps

### Features
- [ ] **Conversation context** — pass full message history to Claude for coherent follow-ups
- [ ] **Streaming responses** — SSE so answers type out word-by-word
- [ ] **Persist chat** — store conversations in `localStorage`
- [ ] **Expand enrichment keywords** — add `claude`, `vite`, `pydantic`, etc.
- [ ] **Export transcript** — download chat as `.txt` or `.pdf`

### Quality
- [ ] **Rate limiting** — add `slowapi` to prevent API key exhaustion
- [ ] **Automated tests** — `pytest` + `httpx` with mocked Anthropic client

### Production
- [ ] **Docker Compose** — single `docker compose up` for both services
- [ ] **Deploy** — backend to AWS Fargate or Railway; frontend to Vercel or Netlify
- [ ] **Set `ALLOWED_ORIGINS`** — restrict CORS to your production domain
