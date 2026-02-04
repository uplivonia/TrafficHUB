import os
import redis
from rq import Worker, Queue, Connection
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
QUEUE_NAME = os.getenv("RQ_QUEUE", "default")

def main():
    conn = redis.from_url(REDIS_URL)
    with Connection(conn):
        worker = Worker([Queue(QUEUE_NAME)])
        worker.work(with_scheduler=True)

if __name__ == "__main__":
    main()
