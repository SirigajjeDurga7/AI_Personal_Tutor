from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.admin import router as admin_router
from app.api.progress import router as progress_router
from app.api.performance import router as performance_router



app = FastAPI(
    title="AI LMS Backend"
)

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(progress_router)
app.include_router(performance_router)
@app.get("/")
async def root():
    return {
        "message": "Backend Running Successfully"
    }