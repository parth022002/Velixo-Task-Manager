from fastapi import APIRouter
from typing import Dict, Any, List
from app.core.database import db_store
from app.ai.agents.chief_of_staff import PlannerAgent

router = APIRouter(prefix="/planner", tags=["Autonomous Daily Planner"])
planner_agent = PlannerAgent()

@router.get("/today")
def get_daily_plan() -> Dict[str, Any]:
    """Retrieves the autonomous daily schedule and time blocks."""
    return planner_agent.generate_daily_plan()

@router.post("/task/{task_id}/status")
def update_task_status(task_id: str, payload: Dict[str, str]) -> Dict[str, Any]:
    """Updates task status (pending, in_progress, completed)."""
    new_status = payload.get("status", "completed")
    data = db_store.read_all()
    
    updated = False
    for task in data.get("tasks", []):
        if task["id"] == task_id:
            task["status"] = new_status
            updated = True
            break
            
    if updated:
        db_store.write_all(data)
        return {"status": "success", "task_id": task_id, "new_status": new_status}
    
    return {"status": "error", "message": "Task not found"}
