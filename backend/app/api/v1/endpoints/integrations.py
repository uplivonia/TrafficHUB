from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.connectors.registry import connector_registry

router = APIRouter()

class IntegrationConnectRequest(BaseModel):
    network: str
    # For real connectors you may store OAuth tokens / API keys encrypted.
    credentials: dict = {}

@router.get("/")
def list_supported():
    return {"supported": sorted(connector_registry.keys())}

@router.post("/connect")
def connect(req: IntegrationConnectRequest):
    if req.network not in connector_registry:
        raise HTTPException(status_code=404, detail="Unknown network")
    # Stub: just validate connector can be created
    connector_cls = connector_registry[req.network]
    connector = connector_cls(credentials=req.credentials)
    return {"status": "ok", "network": req.network, "connector": connector.meta()}
