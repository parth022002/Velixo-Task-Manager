import uuid
from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from app.core.database import db_store
from app.ai.agents.chief_of_staff import PriorityAgent

router = APIRouter(prefix="/github", tags=["GitHub Integration & Webhooks"])

@router.get("/overview")
def get_github_overview() -> Dict[str, Any]:
    """Retrieves current open GitHub PRs, issues, CI build statuses, and sprint releases."""
    return {
        "status": "connected",
        "repository": "madirae/Velixo",
        "open_pull_requests": [
            {
                "id": "pr-104",
                "title": "feat: Add Neon PostgreSQL vector memory & RBAC roles",
                "author": "Parth (Admin)",
                "status": "review_requested",
                "ci_build": "passing",
                "updated_at": "10 mins ago"
            },
            {
                "id": "pr-102",
                "title": "fix: Resolve Universal Capture audio transcript parsing",
                "author": "Alex Rivera",
                "status": "approved",
                "ci_build": "passing",
                "updated_at": "1 hour ago"
            }
        ],
        "open_issues": [
            {
                "id": "issue-45",
                "title": "GPU compute memory allocation bottleneck on Zentrix API",
                "labels": ["bug", "critical", "backend"],
                "assigned_to": "Sarah Jenkins",
                "created_at": "Yesterday"
            },
            {
                "id": "issue-42",
                "title": "Add WebSockets streaming handler for Chief of Staff chat",
                "labels": ["enhancement", "AI"],
                "assigned_to": "David Chen",
                "created_at": "2 days ago"
            }
        ],
        "ci_status": {
            "branch": "main",
            "last_build": "SUCCESS",
            "build_duration": "42s",
            "coverage": "94%"
        }
    }

@router.post("/sync")
def sync_github_tasks() -> Dict[str, Any]:
    """Syncs open GitHub issues into active high-priority Velixo tasks."""
    data = db_store.read_all()

    github_data = get_github_overview()
    synced_tasks = []

    for issue in github_data["open_issues"]:
        task_id = f"gh-{issue['id']}"
        # Check if task already exists
        if not any(t["id"] == task_id for t in data.get("tasks", [])):
            score = PriorityAgent.calculate_score(urgency=9, importance=9, impact=8)
            new_task = {
                "id": task_id,
                "title": f"[GitHub {issue['id']}] {issue['title']}",
                "description": f"Auto-synced from GitHub repository issue {issue['id']}.",
                "domain": "professional",
                "priority": "CRITICAL" if "critical" in issue["labels"] else "HIGH",
                "priority_score": score,
                "urgency": 9,
                "importance": 9,
                "impact": 8,
                "estimated_minutes": 60,
                "status": "pending",
                "due_date": "Today",
                "tags": ["GitHub", "Sync"] + issue["labels"],
                "project_id": "proj-1",
                "assigned_to": "usr-admin"
            }
            data["tasks"].insert(0, new_task)
            synced_tasks.append(new_task)

    db_store.write_all(data)
    return {
        "status": "success",
        "synced_count": len(synced_tasks),
        "synced_tasks": synced_tasks
    }
