Perfect. Let’s lock the final, high-impact intent file—the one you drop into Claude Code and hit run for that “Nirvana moment.”

This version is tightened for:
•	Zero ambiguity
•	Full system generation
•	Demo reliability
•	Immediate wow factor

⸻

🧠 FINAL INTENT FILE — “Nirvana Demo” (Claude Code Ready)

# ============================================================

# INTENT FILE — INTENT-DRIVEN ENGINEERING DEMO SYSTEM

# Purpose: Generate a full-stack AI chatbot system instantly

# Audience: Enterprise engineers (L’Oreal training)

# Mode: Claude Code Interactive Execution

# ============================================================

intent:
name: “Intent-Driven Engineering Chatbot (Nirvana Demo)”

goal: >
Build a complete, production-style chatbot application using a React frontend
and FastAPI backend that integrates with the Anthropic Claude API.
The chatbot must answer questions about Intent-Driven Engineering and
enrich responses with contextual reference links.

experience_goal: >
The system should feel polished, fast, and visually clean so that users
immediately perceive power and clarity when interacting with it.

audience:
- engineers unfamiliar with intent-driven engineering
- architects evaluating AI-assisted development
- enterprise training participants

architecture:
pattern: “Frontend (React) → Backend (FastAPI) → Anthropic API → Enrichment Layer”
principles:
- strict backend ownership of API key
- clean separation of concerns
- production-realistic structure but simple setup

tech_stack:
frontend:
framework: “React (Vite)”
styling:
theme: “modern, minimal, elegant (L’Oreal-inspired UI)”
requirements:
- soft gradients
- rounded chat bubbles
- clean typography
features:
- chat interface (user + assistant bubbles)
- input box with send button
- loading indicator while waiting
- auto-scroll to latest message
- render enriched reference links under responses

```
backend:
  framework: "FastAPI (Python)"
  features:
    - POST /chat endpoint
    - request validation using Pydantic
    - Anthropic API integration
    - enrichment layer (adds learning links)
    - environment variable configuration (.env)
    - CORS enabled for frontend

ai_provider:
  name: "Anthropic Claude"
  model: "claude-3-haiku-20240307"
  configuration:
    - API key loaded from environment variable ANTHROPIC_API_KEY
    - max_tokens: 500
```

api_contract:
endpoint: “/chat”
method: “POST”
request:
{
“message”: “string”
}
response:
{
“answer”: “string”,
“references”: [
{
“title”: “string”,
“url”: “string”
}
]
}

intelligence_layer:
description: >
Enhance responses with curated links based on detected keywords
in the user message or AI response.

```
keyword_mapping:
  - keyword: "intent"
    links:
      - { title: "LearnTeachMaster - Intent-Driven Engineering", url: "https://learnteachmaster.org" }

  - keyword: "anthropic"
    links:
      - { title: "Anthropic Documentation", url: "https://docs.anthropic.com" }

  - keyword: "fastapi"
    links:
      - { title: "FastAPI Docs", url: "https://fastapi.tiangolo.com" }

  - keyword: "react"
    links:
      - { title: "React Documentation", url: "https://react.dev" }
```

backend_logic:
steps:
- receive request
- validate input
- construct Anthropic API payload
- send request to Anthropic API
- extract response text
- run enrichment function
- return structured JSON response

frontend_logic:
steps:
- capture user input
- display user message immediately
- show loading indicator
- call backend /chat endpoint
- render assistant response
- render clickable reference links below response

file_structure:
root:
- backend/
- main.py
- services/
- anthropic_client.py
- enrichment.py
- requirements.txt
- .env.example
- frontend/
- index.html
- package.json
- src/
- main.jsx
- App.jsx
- components/
- ChatWindow.jsx
- MessageBubble.jsx
- styles.css
- README.md

environment:
backend_env:
- ANTHROPIC_API_KEY=your_api_key_here

run_instructions:
backend:
- cd backend
- python -m venv venv
- source venv/bin/activate (or venv\Scripts\activate on Windows)
- pip install -r requirements.txt
- create .env file and add ANTHROPIC_API_KEY
- run: uvicorn main:app –reload

```
frontend:
  - cd frontend
  - npm install
  - npm run dev
```

success_criteria:
- user sends message from UI
- FastAPI receives request
- Anthropic API returns valid response
- response includes enriched reference links
- UI renders answer + links cleanly
- system runs locally with no missing dependencies

# ============================================================

# EXECUTION INSTRUCTIONS FOR CLAUDE CODE

# ============================================================

execution:
mode: “interactive”
instruction: >
Generate the FULL working application described above.
Include all files, code, and configurations.
Do not leave placeholders or TODOs.
Ensure frontend and backend integrate correctly.
Output must be fully runnable locally.

```
Ask clarification questions ONLY if absolutely necessary.
Otherwise proceed directly with full generation.
```

⸻

🔥 How you use this in the room
1.	Open Claude Code
2.	Paste this
3.	Hit run

Then say:

“You don’t need to understand this yet. Just watch.”

Let it build.

Let it run.

Let them use it.

⸻

🎯 What makes this version powerful
•	No fluff → execution-ready
•	Real architecture → credible
•	Visible enrichment → feels intelligent
•	Clean UI → feels premium
•	Backend security → enterprise-safe

⸻

🚀 Next step (when you’re ready)

Now that this is locked, we move to:

👉 Your presentation (Nirvana → Breakdown → Ownership)
👉 With custom visuals in your brand style

Just say:
“presentation”

and I’ll build the full thing exactly how you run it live.