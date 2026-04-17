from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    # TODO: parse and store the resume
    return {"filename": file.filename, "status": "received"}

@router.get("/sample")
async def sample():
    return {"message": "resume routes"}
