import json
import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from app.ai.providers import AIProviderFactory

logger = logging.getLogger(__name__)

class EveningReviewRequest(BaseModel):
    completed_tasks_count: int = 7
    planned_tasks_count: int = 8
    main_distraction: Optional[str] = "Ad-hoc messaging notifications"
    focus_minutes: int = 240

class AICoachAgent:
    """
    Velixo Phase 5 AI Coach Agent.
    Generates an honest end-of-day evening review:
    - % of planned work completed
    - Main distraction pattern analysis
    - Tomorrow's key recommendation
    """

    def generate_evening_review(self, req: EveningReviewRequest) -> Dict[str, Any]:
        completion_pct = round((req.completed_tasks_count / max(1, req.planned_tasks_count)) * 100, 1)

        system_instruction = (
            "You are the Velixo AI Executive Coach. Provide an encouraging yet honest "
            "end-of-day reflection review based on the user's execution metrics."
        )

        prompt = (
            f"Completed Tasks: {req.completed_tasks_count} / {req.planned_tasks_count} ({completion_pct}%)\n"
            f"Focus Time: {req.focus_minutes} minutes\n"
            f"Main Distraction: {req.main_distraction or 'None reported'}\n\n"
            "Return a JSON object with keys:\n"
            "- daily_completion_percentage (number)\n"
            "- performance_tier (string: Exceptional, Solid, Partial)\n"
            "- key_win (string)\n"
            "- distraction_insight (string)\n"
            "- recommendation_for_tomorrow (string)"
        )

        provider = AIProviderFactory.get_provider()
        try:
            raw_res = provider.generate(prompt, system_instruction=system_instruction, json_mode=True)
            return json.loads(raw_res)
        except Exception as e:
            logger.warning(f"AI Coach fallback: {e}")
            return {
                "daily_completion_percentage": completion_pct,
                "performance_tier": "Exceptional" if completion_pct >= 85 else "Solid",
                "key_win": f"Completed {req.completed_tasks_count} high-priority work items across {req.focus_minutes} minutes of deep focus.",
                "distraction_insight": f"Main distraction identified: '{req.main_distraction}'. Recommend batching notification checks.",
                "recommendation_for_tomorrow": "Schedule your hardest architectural focus block before 11:00 AM tomorrow."
            }

ai_coach_agent = AICoachAgent()
