import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, Text, DateTime, ForeignKey, Boolean, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class DBUser(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: f"usr-{uuid.uuid4().hex[:8]}")
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="Developer")  # Admin, Manager, Lead Developer, Developer, Junior Developer
    hierarchy_level = Column(Integer, default=4)
    reports_to = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)

class DBProject(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=lambda: f"proj-{uuid.uuid4().hex[:6]}")
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    domain = Column(String, default="professional")
    progress_percentage = Column(Integer, default=0)
    milestones = Column(JSON, default=list)
    risks = Column(JSON, default=list)
    expected_completion = Column(String, nullable=True)
    delay_probability = Column(Float, default=0.15)
    team_members = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)

class DBTask(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: f"task-{uuid.uuid4().hex[:6]}")
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    domain = Column(String, default="professional")
    priority = Column(String, default="HIGH")  # CRITICAL, HIGH, MEDIUM, LOW
    priority_score = Column(Float, default=85.0)
    urgency = Column(Integer, default=8)
    importance = Column(Integer, default=9)
    impact = Column(Integer, default=9)
    estimated_minutes = Column(Integer, default=45)
    status = Column(String, default="pending")  # pending, in_progress, completed
    due_date = Column(String, nullable=True)
    tags = Column(JSON, default=list)
    project_id = Column(String, nullable=True)
    assigned_to = Column(String, nullable=True)
    energy_required = Column(String, default="high")
    created_at = Column(DateTime, default=datetime.utcnow)

class DBSchedule(Base):
    __tablename__ = "schedules"

    id = Column(String, primary_key=True, default=lambda: f"s-{uuid.uuid4().hex[:6]}")
    time_slot = Column(String, nullable=False)
    title = Column(String, nullable=False)
    category = Column(String, default="Focus Block")
    status = Column(String, default="pending")
    task_id = Column(String, nullable=True)
    energy_level = Column(String, default="high")

class DBKnowledgeNode(Base):
    __tablename__ = "knowledge_nodes"

    id = Column(String, primary_key=True)
    label = Column(String, nullable=False)
    type = Column(String, default="concept")  # project, agent, concept, person, document
    domain = Column(String, default="professional")
    details = Column(Text, nullable=True)

class DBKnowledgeEdge(Base):
    __tablename__ = "knowledge_edges"

    id = Column(String, primary_key=True, default=lambda: f"edge-{uuid.uuid4().hex[:6]}")
    source = Column(String, nullable=False)
    target = Column(String, nullable=False)
    relation = Column(String, nullable=False)

class DBChatMessage(Base):
    __tablename__ = "chat_history"

    id = Column(String, primary_key=True, default=lambda: f"msg-{uuid.uuid4().hex[:6]}")
    sender = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    timestamp = Column(String, default=lambda: datetime.now().isoformat())
    agent_name = Column(String, default="Chief of Staff")
