from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.jira import router as jira_router

app = FastAPI(title="Jira Automation Service")

@app.get("/")
def root():
    return {
        "service": "jira-automation-service",
        "status": "running",
        "docs": "/docs",
        "health": "/health"
    }

app.include_router(health_router)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(jira_router, prefix="/jira", tags=["jira"])
