import requests
from app.services.auth_store import get_auth_context

def create_issue(project_key: str, summary: str, description: str | None, issue_type: str = "Task"):
    access_token, cloud_id = get_auth_context()

    url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "issuetype": {"name": issue_type},
        }
    }

    if description:
        payload["fields"]["description"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {"type": "paragraph", "content": [{"type": "text", "text": description}]}
            ],
        }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    r = requests.post(url, json=payload, headers=headers, timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"Jira API error {r.status_code}: {r.text}")

    data = r.json()
    return {"id": data.get("id"), "key": data.get("key"), "self": data.get("self")}
