import json
import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from app.ai.providers import AIProviderFactory

logger = logging.getLogger(__name__)

class HealthLogRequest(BaseModel):
    sleep_hours: float = 7.5
    water_intake_liters: float = 2.5
    workout_minutes: int = 45
    mood: Optional[str] = "Focused"

class FinanceTrackerRequest(BaseModel):
    item_name: str
    amount: float
    category: str = "Subscription"  # Subscription, EMI, Utility, Savings
    due_date: str = "Monthly on 1st"
    recurring: bool = True

class LearningGoalRequest(BaseModel):
    topic: str  # e.g., "System Design & Distributed Systems"
    target_days: int = 14
    hours_per_day: float = 1.0

class LifeDomainAgentManager:
    """
    Velixo Phase 3 Life Domain Agents:
    Health Manager, Finance Manager, Learning Manager, and Habit Intelligence.
    """

    def process_health_log(self, req: HealthLogRequest) -> Dict[str, Any]:
        # Compute health index
        sleep_score = min(100, (req.sleep_hours / 8.0) * 100)
        water_score = min(100, (req.water_intake_liters / 3.0) * 100)
        workout_score = min(100, (req.workout_minutes / 45.0) * 100)
        overall_health_score = round((sleep_score * 0.4) + (water_score * 0.3) + (workout_score * 0.3), 1)

        nudges = []
        if req.water_intake_liters < 2.5:
            nudges.append("💧 Hydration Nudge: Drink 500ml of water now.")
        if req.sleep_hours < 7.0:
            nudges.append("😴 Sleep Nudge: Plan to wind down 30 minutes earlier tonight.")
        if req.workout_minutes < 30:
            nudges.append("🏃 Motion Nudge: Take a 10-minute walk after your current focus block.")
        if not nudges:
            nudges.append("🌟 Excellent vitality metrics today! Keep up the momentum.")

        return {
            "health_score": overall_health_score,
            "status": "Optimal" if overall_health_score >= 80 else "Needs Attention",
            "metrics": {
                "sleep": f"{req.sleep_hours} hrs",
                "water": f"{req.water_intake_liters} L",
                "workout": f"{req.workout_minutes} mins"
            },
            "nudges": nudges
        }

    def process_finance_item(self, req: FinanceTrackerRequest) -> Dict[str, Any]:
        return {
            "status": "tracked",
            "task_entry": {
                "title": f"Pay {req.item_name} ({req.category}) - ${req.amount:.2f}",
                "priority": "HIGH" if req.category in ["EMI", "Utility"] else "MEDIUM",
                "due_date": req.due_date,
                "recurring": req.recurring
            },
            "finance_summary": f"Logged {req.category} '${req.item_name}' (${req.amount:.2f}) due {req.due_date}."
        }

    def generate_learning_roadmap(self, req: LearningGoalRequest) -> Dict[str, Any]:
        system_instruction = (
            "You are the Velixo AI Learning Manager. Break down the user's learning topic into "
            "a structured multi-day roadmap with daily focus sessions, quizzes, and revision blocks."
        )

        prompt = (
            f"Learning Goal: {req.topic}\n"
            f"Target Duration: {req.target_days} days ({req.hours_per_day} hr/day)\n\n"
            "Return a JSON object with keys:\n"
            "- roadmap_title (string)\n"
            "- estimated_mastery_level (string)\n"
            "- modules (list of objects with day_number, module_title, key_concepts, quiz_question)"
        )

        provider = AIProviderFactory.get_provider()
        try:
            raw_res = provider.generate(prompt, system_instruction=system_instruction, json_mode=True)
            return json.loads(raw_res)
        except Exception as e:
            logger.warning(f"AI Learning Manager fallback: {e}")
            return {
                "roadmap_title": f"Mastery Roadmap: {req.topic}",
                "estimated_mastery_level": "Intermediate Developer Level",
                "modules": [
                    {
                        "day_number": 1,
                        "module_title": f"Core Foundations of {req.topic}",
                        "key_concepts": ["Architecture Basics", "Core Tradeoffs", "Initial Setup"],
                        "quiz_question": f"What is the fundamental design principle behind {req.topic}?"
                    },
                    {
                        "day_number": 2,
                        "module_title": f"Advanced Patterns & Implementation",
                        "key_concepts": ["Scalability", "Error Handling", "Optimization"],
                        "quiz_question": f"How do you handle fault tolerance in {req.topic}?"
                    }
                ]
            }

    def analyze_habit_intelligence(self, completed_tasks: List[str], skipped_tasks: List[str]) -> Dict[str, Any]:
        skipped_set = [t.lower() for t in skipped_tasks]
        adjustments = []

        if any("monday" in t or "workout" in t for t in skipped_set):
            adjustments.append({
                "habit": "Monday Workout",
                "observation": "Habitually skipped on Monday mornings due to weekly start meetings.",
                "suggested_timing": "Move workout session to Tuesday 07:30 AM."
            })
        if any("review" in t or "study" in t for t in skipped_set):
            adjustments.append({
                "habit": "Evening Reading / Review",
                "observation": "Skipped during late evening focus blocks.",
                "suggested_timing": "Shift 20-minute reading block to right after lunch (13:30 PM)."
            })
        if not adjustments:
            adjustments.append({
                "habit": "General Routines",
                "observation": "High completion rate across all tracked habits.",
                "suggested_timing": "Maintain current schedule."
            })

        return {
            "completion_rate": round((len(completed_tasks) / max(1, len(completed_tasks) + len(skipped_tasks))) * 100, 1),
            "detected_adjustments": adjustments
        }

life_domains_agent = LifeDomainAgentManager()
