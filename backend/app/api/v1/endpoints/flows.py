from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Any, List, Dict

from app.services.flow_engine import FlowEngine

router = APIRouter()
engine = FlowEngine()

class FlowNode(BaseModel):
    id: str
    type: str
    config: Dict[str, Any] = Field(default_factory=dict)

class FlowEdge(BaseModel):
    source: str
    target: str

class FlowDefinition(BaseModel):
    name: str
    nodes: List[FlowNode]
    edges: List[FlowEdge]

@router.post("/validate")
def validate_flow(flow: FlowDefinition):
    return engine.validate(flow.model_dump())

@router.post("/dry-run")
def dry_run(flow: FlowDefinition):
    # Stub: does not execute network actions
    return engine.dry_run(flow.model_dump())
