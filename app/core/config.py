from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "jira-automation-service"
    ENV: str = "local"
    BASE_URL: str = "http://127.0.0.1:8000"

    ATLASSIAN_CLIENT_ID: str
    ATLASSIAN_CLIENT_SECRET: str
    ATLASSIAN_REDIRECT_URI: str
    ATLASSIAN_SCOPES: str

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
