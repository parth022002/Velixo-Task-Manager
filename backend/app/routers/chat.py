from fastapi import APIRouter
from typing import Dict, Any
from datetime import datetime
from app.models.schemas import ChatMessage
from app.core.database import db_store
from app.ai.agents.chief_of_staff import chief_of_staff

router = APIRouter(prefix="/chat", tags=["AI Chief of Staff Assistant"])

@router.post("/send")
def send_chat_message(msg: ChatMessage) -> Dict[str, Any]:
    """Conversational endpoint for natural language interaction with the Chief of Staff agent."""
    data = db_store.read_all()
    chat_history = data.get("chat_history", [])
    
    # Save user message
    chat_history.append({"sender": "user", "text": msg.text, "timestamp": datetime.now().isoformat()})
    
    # Generate AI response
    response_text = chief_of_staff.process_chat(msg.text)
    
    # Save assistant message
    ai_msg = {
        "sender": "assistant",
        "text": response_text,
        "timestamp": datetime.now().isoformat(),
        "agent_name": "Chief of Staff"
    }
    chat_history.append(ai_msg)
    
    data["chat_history"] = chat_history
    db_store.write_all(data)
    
    return {
        "user_message": msg.text,
        "reply": ai_msg,
        "history": chat_history[-10:]
    }

@router.get("/history")
def get_chat_history() -> Dict[str, Any]:
    """Retrieves recent conversation history."""
    data = db_store.read_all()
    return {"history": data.get("chat_history", [])}
