from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
async def stats():
    # TODO: return admin statistics
    return {"users": 0, "resumes": 0}
