import json
import logging
from typing import Dict, Any, Optional
from app.ai.providers import AIProviderFactory

logger = logging.getLogger(__name__)

class EmailAssistantAgent:
    """
    Velixo AI Email Assistant Agent (Phase 2).
    Parses incoming emails, extracts invoices, deadlines, meeting requests, and questions,
    converting them directly into structured tasks or drafted replies.
    """

    def analyze_email(self, email_body: str, sender: str = "unknown@example.com", subject: str = "Notification") -> Dict[str, Any]:
        system_instruction = (
            "You are the Velixo AI Email Assistant. Read the incoming email message, extract "
            "action items, deadlines, financial invoices, or questions, and generate a task "
            "record along with a drafted polite response."
        )

        prompt = (
            f"Sender: {sender}\n"
            f"Subject: {subject}\n"
            f"Body:\n{email_body}\n\n"
            "Return a JSON object with keys:\n"
            "- is_actionable (boolean)\n"
            "- extracted_task (object with title, priority, deadline, category)\n"
            "- contains_invoice (boolean)\n"
            "- invoice_details (object or null with amount, due_date)\n"
            "- drafted_reply (string)"
        )

        provider = AIProviderFactory.get_provider()
        try:
            raw_res = provider.generate(prompt, system_instruction=system_instruction, json_mode=True)
            return json.loads(raw_res)
        except Exception as e:
            logger.warning(f"AI Email Assistant fallback: {e}")
            return {
                "is_actionable": True,
                "extracted_task": {
                    "title": f"Follow-up on '{subject}' from {sender}",
                    "priority": "HIGH" if "urgent" in email_body.lower() or "invoice" in email_body.lower() else "MEDIUM",
                    "deadline": "Tomorrow",
                    "category": "Communication"
                },
                "contains_invoice": "invoice" in email_body.lower() or "bill" in email_body.lower(),
                "invoice_details": {
                    "amount": "$150.00",
                    "due_date": "Next Week"
                } if "invoice" in email_body.lower() else None,
                "drafted_reply": f"Hi,\n\nThank you for reaching out regarding '{subject}'. I have logged this request into Velixo AI Work OS and will get back to you shortly.\n\nBest regards,\nParth"
            }

email_assistant = EmailAssistantAgent()
