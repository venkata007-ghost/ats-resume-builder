from fastapi import FastAPI
from .routes import resume, auth, payments, webhook, admin

app = FastAPI(title="ATS Resume Builder API")

app.include_router(resume.router, prefix="/resume", tags=["resume"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(webhook.router, prefix="/webhook", tags=["webhook"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/")
async def root():
    return {"message": "ATS Resume Builder API is running"}

def health():
    return {"status": "running"}