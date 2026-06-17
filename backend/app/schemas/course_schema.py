from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str
    category: str
    difficulty: str
    duration: str
    instructor_id: str


class MaterialCreate(BaseModel):
    module_name: str
    topic_name: str
    video_url: str
    pdf_url: str
    assignment_url: str


class AssignmentCreate(BaseModel):
    title: str
    description: str
    due_date: str
    marks: int


class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: str