from fastapi import APIRouter

router = APIRouter(
    prefix="/performance",
    tags=["Performance"]
)

@router.get("/{student_email}")
async def performance(student_email: str):

    return {
        "student": student_email,
        "quiz_average": 82,
        "completion": 65,
        "last_active": "2026-06-17"
    }