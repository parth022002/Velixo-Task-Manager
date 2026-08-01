from fastapi import APIRouter
from typing import Dict, Any
from app.core.config import settings

router = APIRouter(prefix="/settings", tags=["System Settings & AI Providers"])

@router.get("/status")
def get_provider_status() -> Dict[str, Any]:
    """Returns configuration status for AI providers."""
    return {
        "gemini_active": bool(settings.GEMINI_API_KEY),
        "groq_active": bool(settings.GROQ_API_KEY),
        "openai_active": bool(settings.OPENAI_API_KEY),
        "primary_provider": settings.PRIMARY_AI_PROVIDER,
        "mode": "Live Gemini API" if settings.GEMINI_API_KEY else "Helix Local AI Engine (Free Tier Ready)"
    }

@router.post("/keys")
def update_api_keys(payload: Dict[str, str]) -> Dict[str, Any]:
    """Updates API keys dynamically in runtime settings."""
    if "gemini_api_key" in payload:
        settings.GEMINI_API_KEY = payload["gemini_api_key"]
    if "groq_api_key" in payload:
        settings.GROQ_API_KEY = payload["groq_api_key"]
    if "openai_api_key" in payload:
        settings.OPENAI_API_KEY = payload["openai_api_key"]
        
    return {
        "status": "success",
        "message": "AI Provider keys updated successfully.",
        "gemini_active": bool(settings.GEMINI_API_KEY),
        "groq_active": bool(settings.GROQ_API_KEY)
    }
