from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/users")
async def get_users():

    users = await db.users.find(
        {},
        {"_id": 0}
    ).to_list(100)

    return users


@router.delete("/users/{email}")
async def delete_user(email: str):

    await db.users.delete_one(
        {"email": email}
    )

    return {
        "message": "User deleted"
    }
@router.get("/analytics")
async def analytics():

    total_students = await db.users.count_documents({})
    total_instructors = await db.instructors.count_documents({})
    total_admins = await db.admins.count_documents({})

    return {
        "total_students": total_students,
        "total_instructors": total_instructors,
        "total_admins": total_admins,
        "total_users":
            total_students +
            total_instructors +
            total_admins
    }
@router.post("/settings")
async def save_settings(data: dict):

    await db.settings.insert_one(data)

    return {
        "message": "Settings saved"
    }


@router.get("/settings")
async def get_settings():

    settings = await db.settings.find(
        {},
        {"_id": 0}
    ).to_list(100)

    return settings