import os
import redis
from rq import Queue
from app.core.config import settings

def get_queue() -> Queue:
    conn = redis.from_url(settings.REDIS_URL)
    name = os.getenv("RQ_QUEUE", "default")
    return Queue(name, connection=conn)

def enqueue_job(job_name: str, payload: dict) -> str:
    q = get_queue()
    job = q.enqueue("worker.jobs:run_job", job_name, payload)
    return job.id
