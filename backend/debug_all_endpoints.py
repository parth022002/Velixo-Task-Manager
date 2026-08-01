import sys
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def run_api_debug_suite():
    print("=" * 70)
    print("[API DEBUG SUITE] TESTING ALL VELIXO ENDPOINTS IN DETAIL")
    print("=" * 70)

    endpoints_to_test = [
        ("GET", "/", None),
        ("GET", "/api/notifications/status", None),
        ("GET", "/api/google/status", None),
        ("GET", "/api/google/calendar/events", None),
        ("GET", "/api/google/gmail/tasks", None),
        ("GET", "/api/brief/dashboard", None),
        ("GET", "/api/github/overview", None),
        ("POST", "/api/priority/calculate", {
            "title": "Debug Velixo Endpoints",
            "urgency": 9,
            "importance": 9,
            "impact": 8,
            "estimated_minutes": 30,
            "dependency_count": 0,
            "energy_required": 5,
            "goal_alignment": 9
        }),
        ("POST", "/api/priority/batch-rank", [
            {"title": "Task A", "urgency": 9, "importance": 9},
            {"title": "Task B", "urgency": 5, "importance": 5}
        ]),
        ("POST", "/api/meetings/process-transcript", {
            "title": "Debug Meeting",
            "transcript": "Manager: Finalize system testing by 6 PM today."
        }),
        ("POST", "/api/email/analyze", {
            "sender": "billing@neon.tech",
            "subject": "Invoice Reminder",
            "body": "Invoice #5512 for $120 is due tomorrow."
        }),
        ("POST", "/api/life-domains/health/log", {
            "sleep_hours": 8.0,
            "water_intake_liters": 3.0,
            "workout_minutes": 45
        }),
        ("POST", "/api/life-domains/finance/track", {
            "item_name": "Neon Postgres DB",
            "amount": 49.00,
            "category": "Subscription"
        }),
        ("POST", "/api/life-domains/learning/roadmap", {
            "topic": "FastAPI & React System Architecture",
            "target_days": 7,
            "hours_per_day": 1.5
        }),
        ("POST", "/api/life-domains/habits/analyze", {
            "completed_tasks": ["Morning Focus Block"],
            "skipped_tasks": ["Monday Workout"]
        }),
        ("POST", "/api/research/analyze-text", {
            "title": "Velixo Architecture Paper",
            "content": "Provider-agnostic fallback chain ensures 100% uptime resilience."
        }),
        ("POST", "/api/second-brain/search", {
            "query": "Velixo",
            "top_k": 5
        }),
        ("POST", "/api/predictive/project-risk", {
            "project_name": "Velixo Work OS",
            "total_tasks": 10,
            "completed_tasks": 8,
            "days_until_deadline": 4,
            "daily_workload_hours": 7.5
        }),
        ("POST", "/api/predictive/capacity-decision", {
            "available_hours": 5.0,
            "energy_level": "High",
            "primary_goal": "Debug All Endpoints"
        }),
        ("POST", "/api/automation/trigger", {
            "event_type": "UNPAID_INVOICE",
            "payload": {"id": "INV-100"}
        }),
        ("POST", "/api/coach/evening-review", {
            "completed_tasks_count": 8,
            "planned_tasks_count": 8,
            "focus_minutes": 240,
            "main_distraction": "None"
        }),
        ("POST", "/api/intent/process", {
            "raw_text": "I need to deploy Velixo AI Work OS today"
        }),
        ("POST", "/api/planner/generate", {}),
        ("POST", "/api/chat/message", {
            "message": "What is the status of my daily schedule?"
        }),
        ("GET", "/api/graph/nodes", None)
    ]

    passed_count = 0
    failed_count = 0

    for idx, (method, path, payload) in enumerate(endpoints_to_test, 1):
        try:
            if method == "GET":
                response = client.get(path)
            else:
                response = client.post(path, json=payload)

            if response.status_code in [200, 201]:
                passed_count += 1
                print(f"[{idx:02d}/{len(endpoints_to_test)}] SUCCESS {method} {path} -> HTTP {response.status_code}")
            else:
                failed_count += 1
                print(f"[{idx:02d}/{len(endpoints_to_test)}] FAILED  {method} {path} -> HTTP {response.status_code} | Details: {response.text[:100]}")
        except Exception as e:
            failed_count += 1
            print(f"[{idx:02d}/{len(endpoints_to_test)}] EXCEPTION {method} {path} -> Error: {str(e)}")

    print("\n" + "=" * 70)
    print(f"[SUMMARY] Total Tested: {len(endpoints_to_test)} | Passed: {passed_count} | Failed: {failed_count}")
    print("=" * 70)

if __name__ == "__main__":
    run_api_debug_suite()
