import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from services.anthropic_client import chat
from services.enrichment import enrich

load_dotenv()

_ALLOWED_ORIGINS = os.environ.get(
    "ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:5181"
).split(",")

app = FastAPI(title="Intent-Driven Engineering Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=_ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


class Reference(BaseModel):
    title: str
    url: str


class ChatResponse(BaseModel):
    answer: str
    references: list[Reference]


@app.get("/health")
def health_check():
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        return {"status": "fail", "detail": "API key not configured"}
    try:
        chat("Say 'API key works' in exactly those words.")
        return {"status": "ok"}
    except Exception:
        return {"status": "fail", "detail": "Claude API unreachable"}


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    try:
        answer = chat(req.message)
    except Exception:
        raise HTTPException(status_code=502, detail="AI service unavailable")
    references = enrich(req.message, answer)
    return ChatResponse(answer=answer, references=references)
