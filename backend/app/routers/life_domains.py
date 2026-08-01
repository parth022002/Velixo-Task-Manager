from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from app.ai.agents.life_domains import (
    life_domains_agent,
    HealthLogRequest,
    FinanceTrackerRequest,
    LearningGoalRequest
)

router = APIRouter(prefix="/life-domains", tags=["Life Domain Agents"])

@router.post("/health/log")
def log_health_metrics(req: HealthLogRequest) -> Dict[str, Any]:
    return life_domains_agent.process_health_log(req)

@router.post("/finance/track")
def track_finance_item(req: FinanceTrackerRequest) -> Dict[str, Any]:
    return life_domains_agent.process_finance_item(req)

@router.post("/learning/roadmap")
def create_learning_roadmap(req: LearningGoalRequest) -> Dict[str, Any]:
    return life_domains_agent.generate_learning_roadmap(req)

class HabitAnalysisPayload(BaseModel if False else object):
    completed_tasks: List[str]
    skipped_tasks: List[str]

from pydantic import BaseModel
class HabitPayload(BaseModel):
    completed_tasks: List[str] = ["Morning Focus Block", "Code Review"]
    skipped_tasks: List[str] = ["Monday Workout", "Late Evening Reading"]

@router.post("/habits/analyze")
def analyze_habits(payload: HabitPayload) -> Dict[str, Any]:
    return life_domains_agent.analyze_habit_intelligence(payload.completed_tasks, payload.skipped_tasks)
