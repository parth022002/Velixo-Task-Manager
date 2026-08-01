import json
import logging
from typing import Dict, Any, List
from app.ai.providers import AIProviderFactory

logger = logging.getLogger(__name__)

class UniversalCaptureEngine:
    """Universal Capture Engine: Ingests PDF, Voice, Email, Code, or Text and turns them into structured work items."""

    def __init__(self):
        self.ai_provider = AIProviderFactory.get_provider()

    def process_capture(self, input_type: str, content: str, file_name: str = None) -> Dict[str, Any]:
        """Processes raw captured input and returns extracted tasks, milestones, risks, and project context."""
        system_prompt = """You are Velixo, the AI Chief of Staff. Your job is Universal Capture: extract actionable structured work items from user inputs.
Output strictly valid JSON with this structure:
{
  "summary": "Brief 1-sentence summary of the intent",
  "domain": "professional" or "personal",
  "project_name": "Extracted project name or new proposed project",
  "tasks": [
    {
      "title": "Task title",
      "description": "Task description",
      "priority": "CRITICAL" | "HIGH" | "MEDIUM" | "LOW",
      "urgency": 1-10,
      "importance": 1-10,
      "impact": 1-10,
      "estimated_minutes": 30,
      "due_date": "Today" | "Tomorrow" | "Next Week",
      "tags": ["tag1", "tag2"]
    }
  ],
  "milestones": ["Milestone 1", "Milestone 2"],
  "risks": ["Potential delay risk"],
  "people": ["Name or role"]
}"""

        user_prompt = f"Captured Input Type: {input_type}\nFile/Source: {file_name or 'N/A'}\nContent:\n{content}"

        try:
            raw_response = self.ai_provider.generate(user_prompt, system_instruction=system_prompt, json_mode=True)
            if "```json" in raw_response:
                raw_response = raw_response.split("```json")[1].split("```")[0].strip()
            elif "```" in raw_response:
                raw_response = raw_response.split("```")[1].split("```")[0].strip()
                
            return json.loads(raw_response)
        except Exception as e:
            logger.warning(f"Error parsing capture with LLM provider, using fallback parser: {e}")
            return {
                "summary": f"Captured {input_type} content: {content[:80]}...",
                "domain": "personal" if "personal" in content.lower() or "workout" in content.lower() else "professional",
                "project_name": "Velixo Work",
                "tasks": [
                    {
                        "title": f"Process {input_type.upper()} Action Items: {content[:40]}",
                        "description": f"Extracted from {file_name or input_type}: {content}",
                        "priority": "HIGH",
                        "urgency": 8,
                        "importance": 9,
                        "impact": 8,
                        "estimated_minutes": 45,
                        "due_date": "Today",
                        "tags": [input_type, "Auto-Extracted"]
                    }
                ],
                "milestones": ["Review Extracted Tasks"],
                "risks": ["Unverified dependencies"],
                "people": ["You"]
            }

capture_engine = UniversalCaptureEngine()
