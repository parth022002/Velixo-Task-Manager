from fastapi import APIRouter
from typing import Dict, Any
from app.core.database import db_store
from app.ai.agents.chief_of_staff import ExecutiveBriefAgent

router = APIRouter(prefix="/brief", tags=["Executive Briefing & Analytics"])
brief_agent = ExecutiveBriefAgent()

@router.get("/summary")
def get_executive_brief() -> Dict[str, Any]:
    """Returns AI Chief of Staff Morning Executive Brief, Health & Focus metrics."""
    return brief_agent.generate_brief()

@router.get("/dashboard")
def get_full_dashboard() -> Dict[str, Any]:
    """Aggregates all workspace data: Brief, Projects, Tasks, Schedules, Graph."""
    data = db_store.read_all()
    brief = brief_agent.generate_brief()
    
    return {
        "brief": brief,
        "projects": data.get("projects", []),
        "tasks": data.get("tasks", []),
        "schedules": data.get("schedules", []),
        "knowledge_nodes": data.get("knowledge_nodes", []),
        "knowledge_edges": data.get("knowledge_edges", [])
    }
