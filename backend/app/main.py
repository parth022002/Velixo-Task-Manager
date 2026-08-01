import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import intent, capture, planner, brief, graph, chat, settings as settings_router, auth, hierarchy, github, notifications, google_connect, priority, meetings, email_agent, life_domains, research, second_brain, predictive, automation, ai_coach

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Velixo: Next-Gen AI Work Operating System (AI Chief of Staff)"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(hierarchy.router, prefix=settings.API_V1_STR)
app.include_router(brief.router, prefix=settings.API_V1_STR)
app.include_router(intent.router, prefix=settings.API_V1_STR)
app.include_router(capture.router, prefix=settings.API_V1_STR)
app.include_router(planner.router, prefix=settings.API_V1_STR)
app.include_router(graph.router, prefix=settings.API_V1_STR)
app.include_router(chat.router, prefix=settings.API_V1_STR)
app.include_router(github.router, prefix=settings.API_V1_STR)
app.include_router(notifications.router, prefix=settings.API_V1_STR)
app.include_router(google_connect.router, prefix=settings.API_V1_STR)
app.include_router(priority.router, prefix=settings.API_V1_STR)
app.include_router(meetings.router, prefix=settings.API_V1_STR)
app.include_router(email_agent.router, prefix=settings.API_V1_STR)
app.include_router(life_domains.router, prefix=settings.API_V1_STR)
app.include_router(research.router, prefix=settings.API_V1_STR)
app.include_router(second_brain.router, prefix=settings.API_V1_STR)
app.include_router(predictive.router, prefix=settings.API_V1_STR)
app.include_router(automation.router, prefix=settings.API_V1_STR)
app.include_router(ai_coach.router, prefix=settings.API_V1_STR)
app.include_router(settings_router.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {
        "status": "online",
        "app": settings.PROJECT_NAME,
        "tagline": "Your AI Chief of Staff for Work and Life",
        "version": settings.VERSION,
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
