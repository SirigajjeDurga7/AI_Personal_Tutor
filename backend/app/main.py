from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.admin import router as admin_router
from app.api.progress import router as progress_router
from app.api.performance import router as performance_router
from app.api.reports import router as reports_router
from app.api.dashboard import router as dashboard_router


app = FastAPI(
    title="AI LMS Backend"
)

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(progress_router)
app.include_router(performance_router)
app.include_router(reports_router)
app.include_router(dashboard_router)
@app.get("/")
async def root():
    return {
        "message": "Backend Running Successfully"
    }