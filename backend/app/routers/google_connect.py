from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from app.services.google_service import google_service

router = APIRouter(prefix="/google", tags=["Google Integration"])

@router.get("/status")
def get_google_status() -> Dict[str, Any]:
    return {
        "configured": google_service.is_configured(),
        "client_id_configured": bool(google_service.client_id),
        "auth_url": google_service.get_auth_url()
    }

@router.get("/calendar/events")
def get_calendar_events() -> Dict[str, Any]:
    if not google_service.is_configured():
        raise HTTPException(status_code=400, detail="Google OAuth Client ID & Secret not configured in .env")
    return google_service.get_mock_calendar_events()

@router.get("/gmail/tasks")
def get_gmail_extracted_tasks() -> Dict[str, Any]:
    if not google_service.is_configured():
        raise HTTPException(status_code=400, detail="Google OAuth Client ID & Secret not configured in .env")
    return google_service.get_mock_gmail_tasks()
