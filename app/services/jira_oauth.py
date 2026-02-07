import httpx
from urllib.parse import urlencode
from app.core.config import settings

AUTH_URL = "https://auth.atlassian.com/authorize"
TOKEN_URL = "https://auth.atlassian.com/oauth/token"
ACCESSIBLE_RESOURCES_URL = "https://api.atlassian.com/oauth/token/accessible-resources"

def build_authorize_url(state: str) -> str:
    params = {
        "audience": "api.atlassian.com",
        "client_id": settings.ATLASSIAN_CLIENT_ID,
        "scope": settings.ATLASSIAN_SCOPES,
        "redirect_uri": settings.ATLASSIAN_REDIRECT_URI,
        "state": state,
        "response_type": "code",
        "prompt": "consent",
    }
    return f"{AUTH_URL}?{urlencode(params)}"

async def exchange_code_for_tokens(code: str) -> dict:
    payload = {
        "grant_type": "authorization_code",
        "client_id": settings.ATLASSIAN_CLIENT_ID,
        "client_secret": settings.ATLASSIAN_CLIENT_SECRET,
        "code": code,
        "redirect_uri": settings.ATLASSIAN_REDIRECT_URI,
    }
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.post(TOKEN_URL, json=payload)
    resp.raise_for_status()
    return resp.json()

async def get_accessible_resources(access_token: str) -> list[dict]:
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(ACCESSIBLE_RESOURCES_URL, headers=headers)
    resp.raise_for_status()
    return resp.json()
