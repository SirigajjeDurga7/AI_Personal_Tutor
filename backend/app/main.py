from fastapi import FastAPI
from app.api.courses import router as course_router

app = FastAPI(
    title="AI LMS"
)

app.include_router(course_router)

@app.get("/")
async def root():
    return {
        "message": "Course Module Running"
    }