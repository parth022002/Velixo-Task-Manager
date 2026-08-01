from fastapi import APIRouter
from typing import List
from app.ai.priority_engine import priority_engine, MultiFactorPriorityRequest, MultiFactorPriorityResponse

router = APIRouter(prefix="/priority", tags=["Priority Engine"])

@router.post("/calculate", response_model=MultiFactorPriorityResponse)
def calculate_single_priority(req: MultiFactorPriorityRequest):
    return priority_engine.calculate_priority(req)

@router.post("/batch-rank", response_model=List[MultiFactorPriorityResponse])
def batch_rank_tasks(tasks: List[MultiFactorPriorityRequest]):
    results = [priority_engine.calculate_priority(t) for t in tasks]
    results.sort(key=lambda x: x.score, reverse=True)
    return results
