from fastapi import APIRouter
from bson import ObjectId

from app.database.mongodb import db
from app.models.course import course_document
from app.schemas.course_schema import (
    CourseCreate,
    MaterialCreate,
    AssignmentCreate,
    EnrollmentCreate
)

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


# ----------------------------
# COURSE MANAGEMENT
# ----------------------------

@router.post("/create")
async def create_course(data: CourseCreate):

    course = course_document(data)

    result = await db.courses.insert_one(course)

    return {
        "message": "Course created successfully",
        "course_id": str(result.inserted_id)
    }


@router.get("/")
async def get_courses():

    courses = []

    async for course in db.courses.find():
        course["_id"] = str(course["_id"])
        courses.append(course)

    return courses


@router.get("/{course_id}")
async def get_course(course_id: str):

    course = await db.courses.find_one(
        {"_id": ObjectId(course_id)}
    )

    if not course:
        return {"message": "Course not found"}

    course["_id"] = str(course["_id"])

    return course


@router.put("/{course_id}")
async def update_course(
    course_id: str,
    data: CourseCreate
):

    await db.courses.update_one(
        {"_id": ObjectId(course_id)},
        {"$set": data.model_dump()}
    )

    return {"message": "Course updated successfully"}


@router.delete("/{course_id}")
async def delete_course(course_id: str):

    await db.courses.delete_one(
        {"_id": ObjectId(course_id)}
    )

    return {"message": "Course deleted successfully"}


# ----------------------------
# COURSE MATERIALS
# ----------------------------

@router.post("/material")
async def create_material(data: MaterialCreate):

    result = await db.materials.insert_one(
        data.model_dump()
    )

    return {
        "message": "Material added",
        "material_id": str(result.inserted_id)
    }


@router.get("/material")
async def get_materials():

    materials = []

    async for item in db.materials.find():
        item["_id"] = str(item["_id"])
        materials.append(item)

    return materials


# ----------------------------
# ASSIGNMENTS
# ----------------------------

@router.post("/assignments/create")
async def create_assignment(data: AssignmentCreate):

    result = await db.assignments.insert_one(
        data.model_dump()
    )

    return {
        "message": "Assignment created",
        "assignment_id": str(result.inserted_id)
    }


@router.get("/assignments")
async def get_assignments():

    assignments = []

    async for item in db.assignments.find():
        item["_id"] = str(item["_id"])
        assignments.append(item)

    return assignments


@router.put("/assignments/{assignment_id}")
async def update_assignment(
    assignment_id: str,
    data: AssignmentCreate
):

    await db.assignments.update_one(
        {"_id": ObjectId(assignment_id)},
        {"$set": data.model_dump()}
    )

    return {"message": "Assignment updated"}


# ----------------------------
# ENROLLMENT
# ----------------------------

@router.post("/enroll")
async def enroll_course(data: EnrollmentCreate):

    result = await db.enrollments.insert_one(
        data.model_dump()
    )

    return {
        "message": "Enrollment successful",
        "enrollment_id": str(result.inserted_id)
    }


@router.get("/enrolled")
async def get_enrollments():

    enrollments = []

    async for item in db.enrollments.find():
        item["_id"] = str(item["_id"])
        enrollments.append(item)

    return enrollments