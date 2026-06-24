from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/users")
async def user_report():

    students = await db.users.count_documents({})
    instructors = await db.instructors.count_documents({})
    admins = await db.admins.count_documents({})

    return {
        "students": students,
        "instructors": instructors,
        "admins": admins,
        "total_users": students + instructors + admins
    }


@router.get("/platform")
async def platform_report():

    students = await db.users.count_documents({})
    instructors = await db.instructors.count_documents({})
    admins = await db.admins.count_documents({})

    return {
        "total_users": students + instructors + admins,
        "students": students,
        "instructors": instructors,
        "admins": admins
    }