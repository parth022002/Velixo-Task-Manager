import uuid
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Dict, Any, Optional
from app.models.schemas import UniversalCaptureRequest
from app.core.database import db_store
from app.ai.capture import capture_engine
from app.ai.agents.chief_of_staff import PriorityAgent

router = APIRouter(prefix="/capture", tags=["Universal Capture Engine"])

@router.post("/submit")
def submit_capture(req: UniversalCaptureRequest) -> Dict[str, Any]:
    """Ingests text, audio transcript, PDF content, or URLs into structured work items."""
    extracted = capture_engine.process_capture(req.input_type, req.content, req.file_name)
    
    data = db_store.read_all()
    created_tasks = []
    
    for task_data in extracted.get("tasks", []):
        score = PriorityAgent.calculate_score(
            urgency=task_data.get("urgency", 8),
            importance=task_data.get("importance", 8),
            impact=task_data.get("impact", 8)
        )
        new_task = {
            "id": f"task-{uuid.uuid4().hex[:6]}",
            "title": task_data.get("title", f"Process {req.input_type.upper()}"),
            "description": task_data.get("description", req.content),
            "domain": extracted.get("domain", "professional"),
            "priority": task_data.get("priority", "HIGH"),
            "priority_score": score,
            "urgency": task_data.get("urgency", 8),
            "importance": task_data.get("importance", 8),
            "impact": task_data.get("impact", 8),
            "estimated_minutes": task_data.get("estimated_minutes", 30),
            "status": "pending",
            "due_date": task_data.get("due_date", "Today"),
            "tags": [req.input_type, "Captured"],
            "project_id": "proj-1"
        }
        data["tasks"].insert(0, new_task)
        created_tasks.append(new_task)
        
    db_store.write_all(data)
    
    return {
        "status": "success",
        "input_type": req.input_type,
        "extracted_summary": extracted.get("summary"),
        "created_tasks": created_tasks,
        "project_context": extracted.get("project_name")
    }

@router.post("/file")
async def capture_file(file: UploadFile = File(...)) -> Dict[str, Any]:
    """Handles file uploads (PDFs, Images, Audio) and runs Universal Capture."""
    content_bytes = await file.read()
    text_content = content_bytes.decode("utf-8", errors="ignore")[:3000]
    
    if not text_content.strip():
        text_content = f"Uploaded file: {file.filename} (Binary document containing project specifications and tasks)"

    req = UniversalCaptureRequest(
        input_type="pdf" if file.filename.endswith(".pdf") else "file",
        content=text_content,
        file_name=file.filename
    )
    return submit_capture(req)
