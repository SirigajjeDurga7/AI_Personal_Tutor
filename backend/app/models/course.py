from datetime import datetime


def course_document(data):
    return {
        "title": data.title,
        "description": data.description,
        "category": data.category,
        "difficulty": data.difficulty,
        "duration": data.duration,
        "instructor_id": data.instructor_id,
        "created_at": datetime.utcnow()
    }