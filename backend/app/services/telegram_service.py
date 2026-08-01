import logging
import requests
from typing import Dict, Any, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

class TelegramNotificationService:
    """Service to deliver instant push notifications via Telegram Bot API."""
    
    def __init__(self, token: Optional[str] = None):
        self.token = token or settings.TELEGRAM_BOT_TOKEN
        self.base_url = f"https://api.telegram.org/bot{self.token}" if self.token else None

    def is_configured(self) -> bool:
        return bool(self.token and len(self.token) > 10)

    def send_message(self, chat_id: str, text: str, parse_mode: str = "Markdown") -> Dict[str, Any]:
        """Send a markdown text message to a specific Telegram chat_id or user."""
        if not self.is_configured():
            logger.warning("Telegram Bot Token is not configured. Message skipped.")
            return {"status": "skipped", "reason": "TELEGRAM_BOT_TOKEN_MISSING"}
            
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode
        }
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                logger.info(f"Telegram notification sent successfully to {chat_id}")
                return {"status": "success", "data": res.json()}
            else:
                logger.error(f"Telegram API error ({res.status_code}): {res.text}")
                return {"status": "error", "message": res.text}
        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return {"status": "error", "message": str(e)}

    def send_executive_brief(self, chat_id: str, brief: Dict[str, Any]) -> Dict[str, Any]:
        """Format and send the daily executive brief to Telegram."""
        title = brief.get("title", "⚡ Velixo Daily Executive Brief")
        date_str = brief.get("date", "Today")
        productivity = brief.get("productivity_score", 95)
        top_focus = brief.get("top_focus", "Key Project Execution")
        
        message = (
            f"🤖 *{title}*\n"
            f"📅 *Date*: {date_str}\n"
            f"🎯 *Top Focus*: {top_focus}\n"
            f"📈 *Predicted Output*: {productivity}%\n\n"
            f"👉 [Open Velixo Dashboard](http://localhost:5173)\n\n"
            f"_Sent by Velixo AI Chief of Staff_"
        )
        return self.send_message(chat_id, message)

telegram_service = TelegramNotificationService()
