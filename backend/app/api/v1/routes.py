from fastapi import APIRouter

from app.api.v1.endpoints import auth, integrations, flows, events

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(integrations.router, prefix="/integrations", tags=["integrations"])
api_router.include_router(flows.router, prefix="/flows", tags=["flows"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
