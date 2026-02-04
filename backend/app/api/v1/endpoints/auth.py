from fastapi import APIRouter

router = APIRouter()

# Skeleton endpoints. Replace with real auth (JWT/OAuth/etc.)

@router.post("/login")
def login():
    return {"todo": "implement login"}

@router.post("/signup")
def signup():
    return {"todo": "implement signup"}
