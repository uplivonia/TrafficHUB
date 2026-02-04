from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional
from app.worker.queue import enqueue_job

router = APIRouter()

class PublishRequest(BaseModel):
    network: str
    channel: str
    content: Dict[str, Any]
    schedule_at_iso: Optional[str] = None  # ISO datetime string

@router.post("/publish")
def publish(req: PublishRequest):
    # In real app: persist + validate + schedule.
    job_id = enqueue_job("publish", req.model_dump())
    return {"status": "queued", "job_id": job_id}
