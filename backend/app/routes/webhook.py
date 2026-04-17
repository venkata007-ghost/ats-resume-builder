from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/stripe")
async def stripe_webhook(request: Request):
    # TODO: verify signature and process events
    payload = await request.body()
    return {"received_bytes": len(payload)}
