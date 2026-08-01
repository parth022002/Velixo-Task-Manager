from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.ai.agents.email_assistant import email_assistant

router = APIRouter(prefix="/email", tags=["Email Assistant"])

class EmailAnalysisRequest(BaseModel):
    sender: str = "client@company.com"
    subject: str = "Urgent: Project Milestone Review"
    body: str

@router.post("/analyze")
def analyze_incoming_email(req: EmailAnalysisRequest) -> Dict[str, Any]:
    if not req.body.strip():
        raise HTTPException(status_code=400, detail="Email body text cannot be empty.")
    return email_assistant.analyze_email(req.body, req.sender, req.subject)
