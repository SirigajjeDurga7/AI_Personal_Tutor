from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/admin")
async def admin_dashboard():

    students = await db.users.count_documents({})
    instructors = await db.instructors.count_documents({})
    admins = await db.admins.count_documents({})

    return {
        "total_users": students + instructors + admins,
        "total_students": students,
        "total_instructors": instructors,
        "total_admins": admins,
        "total_courses": 0,
        "ai_requests": 0
    }