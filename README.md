# Jira Automation Service

A backend service built with **FastAPI** to automate Jira operations using **OAuth 2.0 (Atlassian)**.  
This project demonstrates real-world API design, authentication flows, and integration with third-party SaaS platforms (Jira Cloud).

---

## What This Project Does (Current State)

### ✅ Implemented
- FastAPI backend with modular, production-ready structure
- OAuth 2.0 (Atlassian) authentication flow  
  - Authorization Code Grant  
  - Secure state validation  
  - Access token handling  
- Jira Cloud API integration  
  - Fetch accessible Jira resources  
  - Create Jira issues programmatically  
- Health check endpoint for service monitoring  
- Environment-based configuration  
  - Secrets managed via `.env` (never committed)  
  - Public `.env.example` for onboarding  
- Basic test setup using `pytest`  
- Clean Git & security practices  
  - Secrets excluded via `.gitignore`  
  - SSH-based GitHub authentication (multi-account safe)  

---

## High-Level Architecture
```bash
Client (Browser / Postman)
|
| OAuth 2.0 Authorization
v
Atlassian Identity Platform
|
| Access Token
v
Jira Automation Service (FastAPI)
|
| REST API Calls
v
Jira Cloud APIs
```

## Project Structure
```bash
jira-automation-service/
├── app/
│ ├── main.py # FastAPI application entry point
│ ├── api/
│ │ └── routes/
│ │ ├── auth.py # OAuth2 login & callback routes
│ │ ├── jira.py # Jira issue automation endpoints
│ │ └── health.py # Health check endpoint
│ ├── core/
│ │ ├── config.py # Environment & settings management
│ │ └── state.py # In-memory runtime state (temporary)
│ └── services/
│ ├── jira_oauth.py # OAuth2 logic with Atlassian
│ ├── jira_api.py # Jira REST API client
│ └── auth_store.py # Temporary token storage
├── tests/
│ └── test_health.py # Basic service test
├── .env.example # Environment variable template
├── .gitignore # Secrets & local files excluded
├── requirements.txt # Python dependencies
└── README.md


---
```
## Authentication Flow (OAuth 2.0)

1. User hits `/auth/login`
2. Service redirects to Atlassian authorization page
3. User grants permissions (scopes)
4. Atlassian redirects back to `/auth/callback`
5. Authorization code is exchanged for an access token
6. Access token is used to call Jira APIs

This follows the **OAuth 2.0 Authorization Code Grant**, the industry standard for SaaS integrations.

---

## Running the Project Locally

### 1. Clone the repository
```bash
git clone git@github-ashikalishaik:ashikalishaik/jira-automation-service.git
cd jira-automation-service
```
### 2. Create virtual environment & install dependencies
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Configure environment variables
```bash
copy .env.example .env
```
Fill in:

ATLASSIAN_CLIENT_ID

ATLASSIAN_CLIENT_SECRET

ATLASSIAN_REDIRECT_URI

### 4. Run the service
```bash
python -m uvicorn app.main:app --reload
```
### 5. Access
API Docs: http://127.0.0.1:8000/docs

Health Check: http://127.0.0.1:8000/health

## API Testing
Swagger UI (/docs) for interactive testing

Postman for:

OAuth 2.0 flows

Authenticated Jira API calls

End-to-end request validation

## Future Enhancments

These features are intentionally not implemented yet and listed as roadmap items.

Persistent storage (PostgreSQL / NoSQL)

Refresh token management

Role-based access control (RBAC)

Webhooks for event-driven workflows

Email notifications (SMTP / async workers)

Background jobs (queues / workers)

CI/CD pipeline

Containerization & cloud deployment (Docker, AWS)

Multi-tenant support

Observability (logging, metrics, tracing)

# Author

Ashik Ali
Backend • APIs • Cloud • Integrations