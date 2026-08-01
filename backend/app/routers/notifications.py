from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.services.telegram_service import telegram_service
from app.core.config import settings

router = APIRouter(prefix="/notifications", tags=["Notifications"])

class TelegramSendSchema(BaseModel):
    chat_id: str
    message: str

class ExecutiveBriefNotificationSchema(BaseModel):
    chat_id: str
    top_focus: Optional[str] = "High-Impact Product Architecture"
    productivity_score: Optional[int] = 95

@router.get("/status")
def get_notification_status():
    return {
        "telegram_configured": telegram_service.is_configured(),
        "telegram_bot_handle": "@Velixo_Task_Manager_Bot",
        "firebase_configured": bool(settings.VITE_APP_FIREBASE_API_KEY)
    }

@router.post("/telegram/send")
def send_telegram_message(payload: TelegramSendSchema):
    result = telegram_service.send_message(payload.chat_id, payload.message)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@router.post("/telegram/brief")
def send_telegram_executive_brief(payload: ExecutiveBriefNotificationSchema):
    brief_data = {
        "title": "⚡ Velixo Daily Executive Briefing",
        "top_focus": payload.top_focus,
        "productivity_score": payload.productivity_score
    }
    result = telegram_service.send_executive_brief(payload.chat_id, brief_data)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result
