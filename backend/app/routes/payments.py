from fastapi import APIRouter

router = APIRouter()

@router.post("/create")
async def create_payment():
    # TODO: integrate payment gateway
    return {"status": "payment_created"}
