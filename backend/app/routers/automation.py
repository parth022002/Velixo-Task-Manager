from fastapi import APIRouter
from typing import Dict, Any
from app.ai.automation_engine import automation_engine, AutomationTriggerRequest

router = APIRouter(prefix="/automation", tags=["Automation Engine"])

@router.post("/trigger")
def trigger_automation_chain(req: AutomationTriggerRequest) -> Dict[str, Any]:
    return automation_engine.trigger_action_chain(req)
