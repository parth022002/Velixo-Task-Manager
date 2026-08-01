from fastapi import APIRouter
from typing import Dict, Any
from app.ai.predictive import predictive_engine, PredictiveRiskRequest, CapacityDecisionRequest

router = APIRouter(prefix="/predictive", tags=["Predictive Intelligence & Capacity"])

@router.post("/project-risk")
def analyze_project_risk(req: PredictiveRiskRequest) -> Dict[str, Any]:
    return predictive_engine.analyze_project_risk(req)

@router.post("/capacity-decision")
def evaluate_capacity_decision(req: CapacityDecisionRequest) -> Dict[str, Any]:
    return predictive_engine.evaluate_capacity_decision(req)
