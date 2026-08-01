import logging
from typing import Dict, Any, Optional
from urllib.parse import urlencode
from app.core.config import settings

logger = logging.getLogger(__name__)

class GoogleIntegrationService:
    """Service to handle Google OAuth, Calendar 2-Way Sync, and Gmail Task Extraction."""
    
    def __init__(self):
        self.client_id = settings.GOOGLE_CLIENT_ID
        self.client_secret = settings.GOOGLE_CLIENT_SECRET
        self.redirect_uri = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/api/google/callback")
        self.scopes = [
            "https://www.googleapis.com/auth/calendar.readonly",
            "https://www.googleapis.com/auth/calendar.events",
            "https://www.googleapis.com/auth/gmail.readonly"
        ]

    def is_configured(self) -> bool:
        return bool(self.client_id and self.client_secret)

    def get_auth_url(self) -> str:
        """Generate Google OAuth 2.0 authorization consent URL."""
        if not self.is_configured():
            return ""
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": " ".join(self.scopes),
            "access_type": "offline",
            "prompt": "consent"
        }
        return f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"

    def get_mock_calendar_events(self) -> Dict[str, Any]:
        """Return sample connected calendar events when OAuth code is exchanged."""
        return {
            "status": "connected",
            "provider": "Google Calendar API",
            "events": [
                {
                    "id": "evt_101",
                    "summary": "Velixo Product Demo & Stakeholder Review",
                    "start": "10:00 AM",
                    "end": "10:45 AM",
                    "attendees": ["parth@example.com", "sarah@example.com"],
                    "status": "confirmed"
                },
                {
                    "id": "evt_102",
                    "summary": "Deep Work: AI Provider Layer & Vector Sync",
                    "start": "11:00 AM",
                    "end": "12:30 PM",
                    "attendees": ["parth@example.com"],
                    "status": "confirmed"
                }
            ]
        }

    def get_mock_gmail_tasks(self) -> Dict[str, Any]:
        """Return sample auto-extracted email tasks."""
        return {
            "status": "synced",
            "provider": "Gmail API",
            "extracted_tasks": [
                {
                    "subject": "Invoice Approval for Q3 Server Hosting",
                    "from": "billing@neon.tech",
                    "extracted_task": "Review and approve Neon DB Q3 invoice",
                    "priority": "HIGH",
                    "deadline": "Tomorrow 5:00 PM"
                },
                {
                    "subject": "Sprint Review Notes & Next Steps",
                    "from": "lead-dev@company.com",
                    "extracted_task": "Update Velixo GitHub webhook integration test cases",
                    "priority": "MEDIUM",
                    "deadline": "Friday"
                }
            ]
        }

google_service = GoogleIntegrationService()
