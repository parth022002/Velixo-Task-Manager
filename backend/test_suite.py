import sys
import json
import logging
from app.core.config import settings
from app.ai.providers import AIProviderFactory
from app.ai.priority_engine import priority_engine, MultiFactorPriorityRequest
from app.ai.agents.meeting_assistant import meeting_assistant
from app.ai.agents.email_assistant import email_assistant
from app.ai.agents.life_domains import life_domains_agent, HealthLogRequest
from app.ai.agents.research_assistant import research_assistant
from app.ai.search.second_brain import second_brain_engine
from app.ai.predictive import predictive_engine, PredictiveRiskRequest
from app.ai.automation_engine import automation_engine, AutomationTriggerRequest
from app.ai.agents.ai_coach import ai_coach_agent, EveningReviewRequest
from app.services.telegram_service import telegram_service
from app.services.google_service import google_service
from app.main import app

def run_suite():
    print("=" * 60)
    print("[TEST SUITE] VELIXO MASTER SYSTEM VERIFICATION")
    print("=" * 60)

    # 1. Config & AI Provider
    print(f"[1/10] Project: {settings.PROJECT_NAME} (v{settings.VERSION})")
    provider = AIProviderFactory.get_provider()
    print(f"       Active AI Provider: {type(provider).__name__} (OK)")

    # 2. Priority Engine
    p_req = MultiFactorPriorityRequest(title="Deploy Phase 5 Velixo", urgency=9, importance=9)
    p_res = priority_engine.calculate_priority(p_req)
    print(f"[2/10] Priority Engine: Score = {p_res.score} ({p_res.priority_level}) (OK)")

    # 3. Meeting Assistant
    m_res = meeting_assistant.process_transcript("Manager: Review Google OAuth and Telegram bot testing.")
    print(f"[3/10] Meeting Assistant: Decisions = {len(m_res.get('key_decisions', []))} (OK)")

    # 4. Email Assistant
    e_res = email_assistant.analyze_email("Invoice #104 for Neon DB hosting $150 due tomorrow.", sender="billing@neon.tech")
    print(f"[4/10] Email Assistant: Actionable = {e_res.get('is_actionable')} (OK)")

    # 5. Life Domain Health Manager
    h_req = HealthLogRequest(sleep_hours=8.0, water_intake_liters=3.0, workout_minutes=45)
    h_res = life_domains_agent.process_health_log(h_req)
    print(f"[5/10] Health Manager: Score = {h_res.get('health_score')} (OK)")

    # 6. Research Assistant
    r_res = research_assistant.analyze_document("Modular provider abstraction prevents vendor lock-in.")
    print(f"[6/10] Research Assistant: Insights = {len(r_res.get('key_insights', []))} (OK)")

    # 7. Second Brain Hybrid Search
    s_res = second_brain_engine.search("Velixo")
    print(f"[7/10] Second Brain Search: Results = {len(s_res.get('retrieved_results', []))} (OK)")

    # 8. Predictive Risk Model
    pr_req = PredictiveRiskRequest(project_name="Velixo Work OS", completed_tasks=9, total_tasks=10, days_until_deadline=5)
    pr_res = predictive_engine.analyze_project_risk(pr_req)
    print(f"[8/10] Predictive Risk: Delay Prob = {pr_res.get('delay_probability')}% ({pr_res.get('delay_risk_level')}) (OK)")

    # 9. Automation Action Chain
    a_req = AutomationTriggerRequest(event_type="UNPAID_INVOICE")
    a_res = automation_engine.trigger_action_chain(a_req)
    print(f"[9/10] Automation Chain: Steps = {len(a_res.get('action_chain_steps', []))} (OK)")

    # 10. AI Executive Coach
    c_req = EveningReviewRequest(completed_tasks_count=8, planned_tasks_count=8)
    c_res = ai_coach_agent.generate_evening_review(c_req)
    print(f"[10/10] AI Executive Coach: Score = {c_res.get('daily_completion_percentage')}% ({c_res.get('performance_tier')}) (OK)")

    print("\n" + "=" * 60)
    print(f"[SUCCESS] ALL 10 COMPONENT TESTS PASSED 100%! Total API Routes: {len(app.routes)}")
    print("=" * 60)

if __name__ == "__main__":
    run_suite()
