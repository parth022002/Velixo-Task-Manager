import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class CapacityDecisionRequest(BaseModel):
    available_hours: float = 5.0
    energy_level: str = "High"  # High, Medium, Low
    primary_goal: Optional[str] = "Ship Velixo Production Roadmap"

class PredictiveRiskRequest(BaseModel):
    project_name: str
    total_tasks: int = 10
    completed_tasks: int = 4
    days_until_deadline: int = 3
    daily_workload_hours: float = 8.5

class AIPredictiveEngine:
    """
    Velixo Phase 4 Predictive Intelligence & AI Decision Engine.
    Computes project delay probability, workload burnout risk, and capacity reasoning.
    """

    def analyze_project_risk(self, req: PredictiveRiskRequest) -> Dict[str, Any]:
        remaining_tasks = max(0, req.total_tasks - req.completed_tasks)
        completion_pct = (req.completed_tasks / max(1, req.total_tasks)) * 100
        
        # Calculate velocity required vs velocity actual
        velocity_required = remaining_tasks / max(1, req.days_until_deadline)
        
        # Delay Probability Model
        if velocity_required > 3.0 or req.days_until_deadline <= 2:
            delay_prob = 85.0
            delay_risk = "HIGH RISK"
            rec = f"Project '{req.project_name}' requires completing {velocity_required:.1f} tasks/day. Reassign or extend deadline."
        elif velocity_required > 1.5:
            delay_prob = 45.0
            delay_risk = "MODERATE RISK"
            rec = f"Maintain steady pace on '{req.project_name}'. Reserve morning focus blocks."
        else:
            delay_prob = 12.0
            delay_risk = "LOW RISK"
            rec = f"'{req.project_name}' is on track for target completion."

        # Burnout Risk Model
        if req.daily_workload_hours >= 9.0:
            burnout_level = "CRITICAL"
            burnout_warning = "⚠️ Daily workload exceeds 9 hours. High risk of cognitive fatigue."
        elif req.daily_workload_hours >= 7.5:
            burnout_level = "MODERATE"
            burnout_warning = "⚡ Workload is intense. Ensure 15-minute breaks between focus blocks."
        else:
            burnout_level = "LOW"
            burnout_warning = "✅ Work-life balance is well optimized."

        return {
            "project_name": req.project_name,
            "completion_percentage": round(completion_pct, 1),
            "delay_probability": delay_prob,
            "delay_risk_level": delay_risk,
            "burnout_risk_level": burnout_level,
            "burnout_warning": burnout_warning,
            "recommendation": rec
        }

    def evaluate_capacity_decision(self, req: CapacityDecisionRequest) -> Dict[str, Any]:
        # Reason over available capacity
        blocks = []
        if req.energy_level.lower() == "high":
            blocks.append({
                "time_slot": "09:00 - 11:30 (2.5 hrs)",
                "focus_type": "Deep Engineering Work",
                "recommended_task": f"High-Impact execution on '{req.primary_goal}'",
                "priority": "CRITICAL"
            })
            blocks.append({
                "time_slot": "13:00 - 14:30 (1.5 hrs)",
                "focus_type": "System Architecture & Review",
                "recommended_task": "Review PRs, issue sync & documentation",
                "priority": "HIGH"
            })
            blocks.append({
                "time_slot": "15:30 - 16:30 (1.0 hr)",
                "focus_type": "Admin & Communication",
                "recommended_task": "Clear inbox and Telegram notifications",
                "priority": "MEDIUM"
            })
        else:
            blocks.append({
                "time_slot": "10:00 - 11:30 (1.5 hrs)",
                "focus_type": "Moderate Focus Block",
                "recommended_task": f"Refactor & verify components for '{req.primary_goal}'",
                "priority": "HIGH"
            })
            blocks.append({
                "time_slot": "14:00 - 15:30 (1.5 hrs)",
                "focus_type": "Execution & Cleanup",
                "recommended_task": "Document updates, habit log & light review",
                "priority": "MEDIUM"
            })

        return {
            "available_hours": req.available_hours,
            "energy_level": req.energy_level,
            "primary_goal": req.primary_goal,
            "optimized_action_plan": blocks
        }

predictive_engine = AIPredictiveEngine()
