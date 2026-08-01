from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.ai.agents.meeting_assistant import meeting_assistant

router = APIRouter(prefix="/meetings", tags=["Meeting Assistant"])

class TextTranscriptRequest(BaseModel):
    title: Optional[str] = "Team Sync Meeting"
    transcript: str

@router.post("/process-transcript")
def process_meeting_transcript(req: TextTranscriptRequest) -> Dict[str, Any]:
    if not req.transcript.strip():
        raise HTTPException(status_code=400, detail="Transcript text cannot be empty.")
    return meeting_assistant.process_transcript(req.transcript, req.title)

@router.post("/upload-audio")
async def upload_meeting_audio(file: UploadFile = File(...), title: Optional[str] = Form("Recorded Meeting")):
    # Simulated speech-to-text processing for uploaded audio file
    contents = await file.read()
    simulated_transcript = (
        f"Speaker 1 (Manager): We need to ship Velixo Phase 2 Task Intelligence by Friday.\n"
        f"Speaker 2 (Lead Dev): I have configured the Google OAuth credentials and Telegram Bot.\n"
        f"Speaker 1: Great, let's verify the Priority Engine and multi-factor scoring today."
    )
    return meeting_assistant.process_transcript(simulated_transcript, title)
