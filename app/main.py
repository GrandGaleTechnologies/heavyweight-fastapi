from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

storage = {"chat": None}

class Message(BaseModel):
    role: str
    text: str

class Conversation(BaseModel):
    summary: Optional[str] = None
    tone_tags: Optional[List[str]] = []
    topic_tags: Optional[List[str]] = []
    tail_messages: Optional[List[Message]] = []

@app.get("/projects/{project_id}/last-conversation")
def get_last_conversation(project_id: str):
    return storage.get(project_id, {"summary": None, "tone_tags": [], "topic_tags": [], "tail_messages": []})

@app.post("/projects/{project_id}/save-conversation")
def save_conversation(project_id: str, conv: Conversation):
    storage[project_id] = conv.dict()
    return {"ok": True, "conversation_id": 1}

