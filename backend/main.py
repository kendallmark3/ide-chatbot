import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.anthropic_client import chat
from services.enrichment import enrich

load_dotenv()

app = FastAPI(title="Intent-Driven Engineering Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


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
        return {"status": "fail", "api_key": "missing"}
    masked = key[:12] + "..." + key[-4:]
    try:
        result = chat("Say 'API key works' in exactly those words.")
        return {"status": "ok", "api_key": masked, "test_response": result}
    except Exception as e:
        return {"status": "fail", "api_key": masked, "error": str(e)}


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    answer = chat(req.message)
    references = enrich(req.message, answer)
    return ChatResponse(answer=answer, references=references)
