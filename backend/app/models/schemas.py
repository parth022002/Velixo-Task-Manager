from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class UserAuthRequest(BaseModel):
    name: Optional[str] = ""
    email: str
    password: str
    role: Optional[str] = "Developer"  # Admin, Manager, Lead Developer, Developer, Junior Developer
    reports_to: Optional[str] = None

class UserProfile(BaseModel):
    id: str
    name: str
    email: str
    role: str  # Admin, Manager, Lead Developer, Developer, Junior Developer
    hierarchy_level: int = 1
    reports_to: Optional[str] = None
    avatar: Optional[str] = None
    status: str = "active"

class HierarchyAssignRequest(BaseModel):
    user_id: str
    new_role: str
    reports_to: Optional[str] = None

class TaskItem(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = ""
    domain: str = "professional"  # professional vs personal
    priority: str = "HIGH"  # CRITICAL, HIGH, MEDIUM, LOW
    priority_score: float = 85.0
    urgency: int = 8
    importance: int = 9
    impact: int = 9
    estimated_minutes: int = 45
    status: str = "pending"  # pending, in_progress, completed
    due_date: Optional[str] = None
    tags: List[str] = []
    project_id: Optional[str] = None
    assigned_to: Optional[str] = None
    dependencies: List[str] = []
    energy_required: str = "high"

class IntentRequest(BaseModel):
    raw_text: str
    source: str = "natural_language"
    user_context: Optional[Dict[str, Any]] = None

class UniversalCaptureRequest(BaseModel):
    input_type: str
    content: str
    file_name: Optional[str] = None
    domain: Optional[str] = "auto"

class ProjectItem(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    domain: str = "professional"
    progress_percentage: int = 0
    milestones: List[str] = []
    risks: List[str] = []
    expected_completion: Optional[str] = None
    delay_probability: float = 0.15
    team_members: List[str] = []

class ScheduleBlock(BaseModel):
    id: Optional[str] = None
    time_slot: str
    title: str
    category: str
    status: str = "pending"
    task_id: Optional[str] = None
    energy_level: str = "high"

class DailyPlannerResponse(BaseModel):
    date: str
    daily_theme: str
    productivity_prediction: int
    burnout_risk: str
    recommended_break_time: str
    blocks: List[ScheduleBlock]

class ExecutiveBrief(BaseModel):
    date: str
    brief_summary: str
    focus_score: int
    health_score: int
    burnout_risk: str
    total_meetings: int
    total_tasks: int
    critical_tasks: int
    top_priorities: List[TaskItem]
    delayed_projects: List[Dict[str, Any]]

class KnowledgeNode(BaseModel):
    id: str
    label: str
    type: str
    domain: str
    details: Optional[str] = ""

class KnowledgeEdge(BaseModel):
    source: str
    target: str
    relation: str

class KnowledgeGraphResponse(BaseModel):
    nodes: List[KnowledgeNode]
    edges: List[KnowledgeEdge]

class ChatMessage(BaseModel):
    sender: str
    text: str
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    agent_name: Optional[str] = "Chief of Staff"
