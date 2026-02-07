from typing import Tuple

# import the same store from auth route
from app.api.routes.auth import OAUTH_STORE

def get_auth_context() -> Tuple[str, str]:
    """
    Returns (access_token, cloud_id)
    Raises error if not connected.
    """
    access_token = OAUTH_STORE.get("access_token")
    cloud_id = OAUTH_STORE.get("cloud_id")

    if not access_token or not cloud_id:
        raise RuntimeError("Not authenticated. Visit /auth/login and finish OAuth.")

    return access_token, cloud_id
