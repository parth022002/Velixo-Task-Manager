import logging
from typing import Dict, Any, List
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class MultiFactorPriorityRequest(BaseModel):
    title: str
    urgency: int  # 1 - 10
    importance: int  # 1 - 10
    impact: int = 5  # 1 - 10
    estimated_minutes: int = 30
    dependency_count: int = 0
    energy_required: int = 5  # 1 - 10
    goal_alignment: int = 7  # 1 - 10

class MultiFactorPriorityResponse(BaseModel):
    title: str
    score: float  # Normalized 0 - 100
    priority_level: str  # CRITICAL, HIGH, MEDIUM, LOW
    recommendation: str
    breakdown: Dict[str, float]

class AIPriorityEngine:
    """
    Velixo PRD Multi-Factor Priority Engine.
    Computes dynamic priority score based on:
    Score = (Urgency x 0.25) + (Importance x 0.25) + (Impact x 0.20) + (Goal Alignment x 0.15) - (Dependency Risk x 0.05) + (Efficiency Bonus x 0.10)
    """

    @staticmethod
    def calculate_priority(req: MultiFactorPriorityRequest) -> MultiFactorPriorityResponse:
        # Base components (scaled 0 - 10)
        u_score = req.urgency * 2.5
        imp_score = req.importance * 2.5
        impact_score = req.impact * 2.0
        goal_score = req.goal_alignment * 1.5

        # Dependency penalty (more blockers = lower initial execution rank)
        dep_penalty = min(req.dependency_count * 2.5, 10.0)

        # Quick Win Bonus (tasks under 30 mins get slight boost)
        quick_win = 5.0 if req.estimated_minutes <= 30 else 0.0

        raw_score = u_score + imp_score + impact_score + goal_score - dep_penalty + quick_win
        final_score = round(max(0.0, min(100.0, raw_score)), 1)

        # Priority Level Designation
        if final_score >= 80.0:
            level = "CRITICAL"
            rec = "Execute immediately in today's first deep work block."
        elif final_score >= 60.0:
            level = "HIGH"
            rec = "Schedule in today's prime focus window."
        elif final_score >= 40.0:
            level = "MEDIUM"
            rec = "Fit into execution or secondary blocks."
        else:
            level = "LOW"
            rec = "Delegate, backlog, or complete in low-energy time slots."

        return MultiFactorPriorityResponse(
            title=req.title,
            score=final_score,
            priority_level=level,
            recommendation=rec,
            breakdown={
                "urgency_weight": u_score,
                "importance_weight": imp_score,
                "impact_weight": impact_score,
                "goal_alignment": goal_score,
                "dependency_penalty": dep_penalty,
                "quick_win_bonus": quick_win
            }
        )

priority_engine = AIPriorityEngine()
