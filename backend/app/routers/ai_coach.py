from fastapi import APIRouter
from typing import Dict, Any
from app.ai.agents.ai_coach import ai_coach_agent, EveningReviewRequest

router = APIRouter(prefix="/coach", tags=["AI Executive Coach"])

@router.post("/evening-review")
def get_evening_review(req: EveningReviewRequest) -> Dict[str, Any]:
    return ai_coach_agent.generate_evening_review(req)
