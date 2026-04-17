from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    # TODO: implement authentication
    return {"message": "login endpoint (stub)"}

@router.post("/register")
async def register():
    return {"message": "register endpoint (stub)"}
