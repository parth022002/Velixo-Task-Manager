import uuid
from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from app.models.schemas import IntentRequest, TaskItem
from app.core.database import db_store
from app.ai.capture import capture_engine
from app.ai.agents.chief_of_staff import PriorityAgent

router = APIRouter(prefix="/intent", tags=["Intent Management"])

@router.post("/process")
def process_intent(req: IntentRequest) -> Dict[str, Any]:
    """Processes user intent in natural language without manual task creation."""
    extracted = capture_engine.process_capture("natural_language_intent", req.raw_text)
    
    data = db_store.read_all()
    created_tasks = []
    
    for task_data in extracted.get("tasks", []):
        score = PriorityAgent.calculate_score(
            urgency=task_data.get("urgency", 7),
            importance=task_data.get("importance", 8),
            impact=task_data.get("impact", 8)
        )
        new_task = {
            "id": f"task-{uuid.uuid4().hex[:6]}",
            "title": task_data.get("title", "New Intent Task"),
            "description": task_data.get("description", req.raw_text),
            "domain": extracted.get("domain", "professional"),
            "priority": task_data.get("priority", "HIGH"),
            "priority_score": score,
            "urgency": task_data.get("urgency", 7),
            "importance": task_data.get("importance", 8),
            "impact": task_data.get("impact", 8),
            "estimated_minutes": task_data.get("estimated_minutes", 45),
            "status": "pending",
            "due_date": task_data.get("due_date", "Today"),
            "tags": task_data.get("tags", ["Intent-Extracted"]),
            "project_id": "proj-1",
            "energy_required": "high"
        }
        data["tasks"].insert(0, new_task)
        created_tasks.append(new_task)
        
    db_store.write_all(data)
    
    return {
        "status": "success",
        "intent_summary": extracted.get("summary"),
        "created_tasks": created_tasks,
        "risks": extracted.get("risks", []),
        "milestones": extracted.get("milestones", [])
    }
