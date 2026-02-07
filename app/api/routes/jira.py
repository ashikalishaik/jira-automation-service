from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.jira_api import create_issue

router = APIRouter(prefix="/jira", tags=["jira"])

class CreateIssueRequest(BaseModel):
    project_key: str
    summary: str
    description: str | None = None
    issue_type: str = "Task"  # Task / Bug / Story etc.

@router.post("/issues")
def create_issue_endpoint(payload: CreateIssueRequest):
    try:
        return create_issue(
            project_key=payload.project_key,
            summary=payload.summary,
            description=payload.description,
            issue_type=payload.issue_type,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
