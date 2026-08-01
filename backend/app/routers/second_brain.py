from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from app.ai.search.second_brain import second_brain_engine, SecondBrainSearchRequest

router = APIRouter(prefix="/second-brain", tags=["Second Brain Search"])

@router.post("/search")
def search_captured_memory(req: SecondBrainSearchRequest) -> Dict[str, Any]:
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Search query cannot be empty.")
    return second_brain_engine.search(req.query, req.top_k)
