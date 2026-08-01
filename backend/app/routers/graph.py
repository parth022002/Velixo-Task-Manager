from fastapi import APIRouter
from typing import Dict, Any
from app.core.database import db_store

router = APIRouter(prefix="/graph", tags=["Knowledge Graph Engine"])

@router.get("/data")
def get_knowledge_graph() -> Dict[str, Any]:
    """Retrieves nodes and directional edges representing the interconnected work-life graph."""
    data = db_store.read_all()
    return {
        "nodes": data.get("knowledge_nodes", []),
        "edges": data.get("knowledge_edges", [])
    }
