import json
import logging
from typing import List, Dict, Any
from app.core.database import db_store

logger = logging.getLogger(__name__)

class SemanticMemoryEngine:
    """Persistent Long-Term Memory and Retrieval-Augmented Generation Engine."""
    
    def __init__(self):
        pass
        
    def add_memory(self, memory_type: str, content: str, metadata: Dict[str, Any] = None):
        data = db_store.read_all()
        memories = data.get("memories", [])
        memories.append({
            "type": memory_type,
            "content": content,
            "metadata": metadata or {}
        })
        data["memories"] = memories
        db_store.write_all(data)

    def search_memory(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Simple keyword & semantic relevance ranking across database projects, tasks, and memory notes."""
        data = db_store.read_all()
        query_words = set(query.lower().split())
        
        results = []
        
        # Search Projects
        for proj in data.get("projects", []):
            text = f"{proj['title']} {proj['description']}".lower()
            score = sum(1 for w in query_words if w in text)
            if score > 0:
                results.append({"type": "project", "title": proj["title"], "snippet": proj["description"], "score": score})
                
        # Search Tasks
        for task in data.get("tasks", []):
            text = f"{task['title']} {task.get('description', '')} {' '.join(task.get('tags', []))}".lower()
            score = sum(1 for w in query_words if w in text)
            if score > 0:
                results.append({"type": "task", "title": task["title"], "snippet": task.get("description", ""), "score": score})

        # Sort by relevance score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:limit]

memory_engine = SemanticMemoryEngine()
