class JiraState:
    access_token: str | None = None
    refresh_token: str | None = None
    cloud_id: str | None = None
    site_url: str | None = None

jira_state = JiraState()
