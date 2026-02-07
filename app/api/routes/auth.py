import secrets
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.services.jira_oauth import build_authorize_url, exchange_code_for_tokens, get_accessible_resources

router = APIRouter(tags=["auth"])

# TEMP: in-memory store (we will move to DB later)
OAUTH_STORE = {}

@router.get("/auth/login")
def auth_login():
    state = secrets.token_urlsafe(16)
    url = build_authorize_url(state)
    OAUTH_STORE["state"] = state
    return RedirectResponse(url)

@router.get("/auth/callback")
async def auth_callback(code: str, state: str):
    if state != OAUTH_STORE.get("state"):
        return {"error": "Invalid state"}

    tokens = await exchange_code_for_tokens(code)
    access_token = tokens["access_token"]

    resources = await get_accessible_resources(access_token)

    # pick the first site (most people have one)
    site = resources[0]
    cloud_id = site["id"]
    site_url = site["url"]

    # store for now (later we persist in DB/Redis)
    OAUTH_STORE["tokens"] = tokens
    OAUTH_STORE["access_token"] = access_token
    OAUTH_STORE["cloud_id"] = cloud_id
    OAUTH_STORE["site_url"] = site_url
    OAUTH_STORE["resources"] = resources

    return {
        "message": "Connected to Atlassian successfully",
        "cloud_id": cloud_id,
        "site_url": site_url,
        "scopes": site.get("scopes", []),
    }
