from fastapi import FastAPI
from app.api.ai import router as ai_router

app = FastAPI(
    title="AI LMS - AI Module"
)

app.include_router(ai_router)

@app.get("/")
async def root():
    return {
        "message": "AI Module Running"
    }