import os
import json
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings
from app.models.orm_models import (
    Base, DBUser, DBProject, DBTask, DBSchedule, DBKnowledgeNode, DBKnowledgeEdge, DBChatMessage
)

logger = logging.getLogger(__name__)

# Neon PostgreSQL Database Engine Setup
try:
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True, pool_size=10, max_overflow=20)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    IS_POSTGRES = True
    logger.info(f"Connected to Neon PostgreSQL Database successfully: {settings.DATABASE_URL[:40]}...")
except Exception as e:
    logger.warning(f"Failed to connect to Neon PostgreSQL, falling back to local store: {e}")
    engine = None
    SessionLocal = None
    IS_POSTGRES = False

class VelixoStore:
    """Unified Database store supporting Neon PostgreSQL and local fallback."""

    def __init__(self):
        self.filepath = os.path.join(os.getcwd(), "velixo_store.json")
        self._initialize()

    def _initialize(self):
        if IS_POSTGRES and engine:
            try:
                # Create all tables in Neon PostgreSQL
                Base.metadata.create_all(bind=engine)
                db: Session = SessionLocal()
                try:
                    # Check if users table is empty, seed if so
                    if db.query(DBUser).count() == 0:
                        logger.info("Seeding initial Velixo data into Neon PostgreSQL...")
                        self._seed_postgres(db)
                finally:
                    db.close()
            except Exception as e:
                logger.error(f"Error initializing Neon PostgreSQL tables: {e}")

        # Local JSON backup initialization
        if not os.path.exists(self.filepath):
            self._write_json(self._get_default_seed())

    def _seed_postgres(self, db: Session):
        seed = self._get_default_seed()
        
        # Seed Users
        for u in seed["users"]:
            db_u = DBUser(
                id=u["id"],
                name=u["name"],
                email=u["email"],
                password=u["password"],
                role=u["role"],
                hierarchy_level=u["hierarchy_level"],
                reports_to=u["reports_to"],
                avatar=u["avatar"],
                status=u["status"]
            )
            db.add(db_u)

        # Seed Projects
        for p in seed["projects"]:
            db_p = DBProject(
                id=p["id"],
                title=p["title"],
                description=p["description"],
                domain=p["domain"],
                progress_percentage=p["progress_percentage"],
                milestones=p["milestones"],
                risks=p["risks"],
                expected_completion=p["expected_completion"],
                delay_probability=p["delay_probability"],
                team_members=p["team_members"]
            )
            db.add(db_p)

        # Seed Tasks
        for t in seed["tasks"]:
            db_t = DBTask(
                id=t["id"],
                title=t["title"],
                description=t["description"],
                domain=t["domain"],
                priority=t["priority"],
                priority_score=t["priority_score"],
                urgency=t["urgency"],
                importance=t["importance"],
                impact=t["impact"],
                estimated_minutes=t["estimated_minutes"],
                status=t["status"],
                due_date=t["due_date"],
                tags=t["tags"],
                project_id=t["project_id"],
                assigned_to=t.get("assigned_to"),
                energy_required=t.get("energy_required", "high")
            )
            db.add(db_t)

        # Seed Schedules
        for s in seed["schedules"]:
            db_s = DBSchedule(
                id=s["id"],
                time_slot=s["time_slot"],
                title=s["title"],
                category=s["category"],
                status=s["status"],
                energy_level=s["energy_level"]
            )
            db.add(db_s)

        # Seed Knowledge Nodes
        for n in seed["knowledge_nodes"]:
            db_n = DBKnowledgeNode(
                id=n["id"],
                label=n["label"],
                type=n["type"],
                domain=n["domain"],
                details=n["details"]
            )
            db.add(db_n)

        # Seed Knowledge Edges
        for e in seed["knowledge_edges"]:
            db_e = DBKnowledgeEdge(
                id=f"edge-{e['source']}-{e['target']}",
                source=e["source"],
                target=e["target"],
                relation=e["relation"]
            )
            db.add(db_e)

        # Seed Chat Messages
        for m in seed["chat_history"]:
            db_m = DBChatMessage(
                sender=m["sender"],
                text=m["text"],
                timestamp=m["timestamp"],
                agent_name=m.get("agent_name", "Chief of Staff")
            )
            db.add(db_m)

        db.commit()
        logger.info("Neon PostgreSQL seeding completed successfully!")

    def _get_default_seed(self) -> Dict[str, Any]:
        return {
            "users": [
                {
                    "id": "usr-admin",
                    "name": "Parth (Admin)",
                    "email": "parth@velixo.ai",
                    "password": "adminpassword123",
                    "role": "Admin",
                    "hierarchy_level": 1,
                    "reports_to": None,
                    "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Admin",
                    "status": "active"
                },
                {
                    "id": "usr-mgr-1",
                    "name": "Sarah Jenkins",
                    "email": "sarah@velixo.ai",
                    "password": "password123",
                    "role": "Manager",
                    "hierarchy_level": 2,
                    "reports_to": "usr-admin",
                    "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah",
                    "status": "active"
                },
                {
                    "id": "usr-lead-1",
                    "name": "Alex Rivera",
                    "email": "alex@velixo.ai",
                    "password": "password123",
                    "role": "Lead Developer",
                    "hierarchy_level": 3,
                    "reports_to": "usr-mgr-1",
                    "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Alex",
                    "status": "active"
                },
                {
                    "id": "usr-dev-1",
                    "name": "David Chen",
                    "email": "david@velixo.ai",
                    "password": "password123",
                    "role": "Developer",
                    "hierarchy_level": 4,
                    "reports_to": "usr-lead-1",
                    "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=David",
                    "status": "active"
                },
                {
                    "id": "usr-jr-1",
                    "name": "Rohan Sharma",
                    "email": "rohan@velixo.ai",
                    "password": "password123",
                    "role": "Junior Developer",
                    "hierarchy_level": 5,
                    "reports_to": "usr-dev-1",
                    "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Rohan",
                    "status": "active"
                }
            ],
            "projects": [
                {
                    "id": "proj-1",
                    "title": "Velixo AI Work OS Engine",
                    "description": "AI Chief of Staff for Work and Life delivering intent management and autonomous planning.",
                    "domain": "professional",
                    "progress_percentage": 75,
                    "milestones": ["Architecture Design", "Universal Capture Engine", "Velixo Glassmorphic Visual Dashboard"],
                    "risks": ["Model Context Window limits"],
                    "expected_completion": "2026-08-15",
                    "delay_probability": 0.10,
                    "team_members": ["Parth (Admin)", "Sarah Jenkins", "Alex Rivera"]
                },
                {
                    "id": "proj-2",
                    "title": "Zentrix Startup & Paper",
                    "description": "Next-gen deep learning platform and paper launch.",
                    "domain": "professional",
                    "progress_percentage": 40,
                    "milestones": ["Abstract & Intro", "Model Benchmark", "Public Launch"],
                    "risks": ["GPU compute availability"],
                    "expected_completion": "2026-09-01",
                    "delay_probability": 0.25,
                    "team_members": ["David Chen", "Rohan Sharma"]
                }
            ],
            "tasks": [
                {
                    "id": "task-101",
                    "title": "Build Velixo Role-Based Access Control & User Auth",
                    "description": "Implement authentication, login, registration, and organizational hierarchy builder.",
                    "domain": "professional",
                    "priority": "CRITICAL",
                    "priority_score": 98.0,
                    "urgency": 10,
                    "importance": 10,
                    "impact": 10,
                    "estimated_minutes": 45,
                    "status": "completed",
                    "due_date": "Today",
                    "tags": ["RBAC", "Auth", "Hierarchy"],
                    "project_id": "proj-1",
                    "assigned_to": "usr-admin",
                    "energy_required": "high"
                },
                {
                    "id": "task-102",
                    "title": "Finalize Universal Capture Engine & Intent Parser",
                    "description": "Multimodal ingestion pipeline for text, PDFs, audio transcripts, and links.",
                    "domain": "professional",
                    "priority": "HIGH",
                    "priority_score": 88.0,
                    "urgency": 8,
                    "importance": 9,
                    "impact": 9,
                    "estimated_minutes": 60,
                    "status": "in_progress",
                    "due_date": "Today",
                    "tags": ["Capture", "NL"],
                    "project_id": "proj-1",
                    "assigned_to": "usr-lead-1",
                    "energy_required": "high"
                }
            ],
            "schedules": [
                {"id": "s-1", "time_slot": "09:00 - 10:30", "title": "Deep Work: Velixo Architecture & Auth Hierarchy", "category": "Focus Block", "status": "completed", "energy_level": "high"},
                {"id": "s-2", "time_slot": "10:30 - 11:30", "title": "Team Organizational Hierarchy Review", "category": "Execution Block", "status": "in_progress", "energy_level": "high"}
            ],
            "knowledge_nodes": [
                {"id": "node-1", "label": "Velixo AI Work OS", "type": "project", "domain": "professional", "details": "Velixo Core Chief of Staff System"},
                {"id": "node-2", "label": "Engineering Team Hierarchy", "type": "concept", "domain": "professional", "details": "Admin -> Manager -> Lead -> Dev -> Jr Dev"}
            ],
            "knowledge_edges": [
                {"source": "node-1", "target": "node-2", "relation": "managed_by"}
            ],
            "chat_history": [
                {"sender": "assistant", "text": "Good morning Parth! I'm Velixo. User registration, login, roles (Admin, Manager, Lead Dev, Developer, Junior Dev), and reporting hierarchy management have been connected to Neon PostgreSQL.", "timestamp": datetime.now().isoformat()}
            ]
        }

    def read_all(self) -> Dict[str, Any]:
        if IS_POSTGRES and SessionLocal:
            try:
                db: Session = SessionLocal()
                try:
                    users = db.query(DBUser).all()
                    projects = db.query(DBProject).all()
                    tasks = db.query(DBTask).all()
                    schedules = db.query(DBSchedule).all()
                    nodes = db.query(DBKnowledgeNode).all()
                    edges = db.query(DBKnowledgeEdge).all()
                    chat = db.query(DBChatMessage).all()

                    return {
                        "users": [
                            {
                                "id": u.id, "name": u.name, "email": u.email, "password": u.password,
                                "role": u.role, "hierarchy_level": u.hierarchy_level, "reports_to": u.reports_to,
                                "avatar": u.avatar, "status": u.status
                            } for u in users
                        ],
                        "projects": [
                            {
                                "id": p.id, "title": p.title, "description": p.description, "domain": p.domain,
                                "progress_percentage": p.progress_percentage, "milestones": p.milestones or [],
                                "risks": p.risks or [], "expected_completion": p.expected_completion,
                                "delay_probability": p.delay_probability, "team_members": p.team_members or []
                            } for p in projects
                        ],
                        "tasks": [
                            {
                                "id": t.id, "title": t.title, "description": t.description, "domain": t.domain,
                                "priority": t.priority, "priority_score": t.priority_score, "urgency": t.urgency,
                                "importance": t.importance, "impact": t.impact, "estimated_minutes": t.estimated_minutes,
                                "status": t.status, "due_date": t.due_date, "tags": t.tags or [],
                                "project_id": t.project_id, "assigned_to": t.assigned_to, "energy_required": t.energy_required
                            } for t in tasks
                        ],
                        "schedules": [
                            {
                                "id": s.id, "time_slot": s.time_slot, "title": s.title, "category": s.category,
                                "status": s.status, "task_id": s.task_id, "energy_level": s.energy_level
                            } for s in schedules
                        ],
                        "knowledge_nodes": [
                            {"id": n.id, "label": n.label, "type": n.type, "domain": n.domain, "details": n.details} for n in nodes
                        ],
                        "knowledge_edges": [
                            {"source": e.source, "target": e.target, "relation": e.relation} for e in edges
                        ],
                        "chat_history": [
                            {"sender": m.sender, "text": m.text, "timestamp": m.timestamp, "agent_name": m.agent_name} for m in chat
                        ]
                    }
                finally:
                    db.close()
            except Exception as e:
                logger.error(f"Error querying Neon PostgreSQL, falling back to local file: {e}")

        return self._read_json()

    def write_all(self, data: Dict[str, Any]):
        if IS_POSTGRES and SessionLocal:
            try:
                db: Session = SessionLocal()
                try:
                    # Sync Users
                    if "users" in data:
                        for u in data["users"]:
                            existing = db.query(DBUser).filter(DBUser.id == u["id"]).first()
                            if existing:
                                existing.name = u["name"]
                                existing.role = u.get("role", existing.role)
                                existing.hierarchy_level = u.get("hierarchy_level", existing.hierarchy_level)
                                existing.reports_to = u.get("reports_to", existing.reports_to)
                                existing.status = u.get("status", existing.status)
                            else:
                                new_u = DBUser(
                                    id=u["id"], name=u["name"], email=u["email"], password=u["password"],
                                    role=u.get("role", "Developer"), hierarchy_level=u.get("hierarchy_level", 4),
                                    reports_to=u.get("reports_to"), avatar=u.get("avatar"), status=u.get("status", "active")
                                )
                                db.add(new_u)

                    # Sync Tasks
                    if "tasks" in data:
                        for t in data["tasks"]:
                            existing_t = db.query(DBTask).filter(DBTask.id == t["id"]).first()
                            if existing_t:
                                existing_t.status = t.get("status", existing_t.status)
                                existing_t.priority_score = t.get("priority_score", existing_t.priority_score)
                            else:
                                new_t = DBTask(
                                    id=t["id"], title=t["title"], description=t.get("description"),
                                    domain=t.get("domain", "professional"), priority=t.get("priority", "HIGH"),
                                    priority_score=t.get("priority_score", 85.0), urgency=t.get("urgency", 8),
                                    importance=t.get("importance", 9), impact=t.get("impact", 9),
                                    estimated_minutes=t.get("estimated_minutes", 45), status=t.get("status", "pending"),
                                    due_date=t.get("due_date"), tags=t.get("tags", []), project_id=t.get("project_id"),
                                    assigned_to=t.get("assigned_to"), energy_required=t.get("energy_required", "high")
                                )
                                db.add(new_t)

                    # Sync Chat
                    if "chat_history" in data:
                        existing_chat_count = db.query(DBChatMessage).count()
                        if len(data["chat_history"]) > existing_chat_count:
                            for m in data["chat_history"][existing_chat_count:]:
                                new_msg = DBChatMessage(
                                    sender=m["sender"], text=m["text"],
                                    timestamp=m.get("timestamp", datetime.now().isoformat()),
                                    agent_name=m.get("agent_name", "Chief of Staff")
                                )
                                db.add(new_msg)

                    db.commit()
                finally:
                    db.close()
            except Exception as e:
                logger.error(f"Error syncing data to Neon PostgreSQL: {e}")

        # Always write to local backup JSON as well
        self._write_json(data)

    def _read_json(self) -> Dict[str, Any]:
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error reading local file: {e}")
            return self._get_default_seed()

    def _write_json(self, data: Dict[str, Any]):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Error writing local file: {e}")

db_store = VelixoStore()
