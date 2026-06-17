from fastapi import APIRouter

router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)

@router.get("/{email}")
async def get_progress(email: str):

    return {
        "email": email,
        "courses_enrolled": 5,
        "completed_courses": 2,
        "quiz_scores": [80, 90, 75],
        "study_hours": 25,
        "completion_percentage": 40
    }