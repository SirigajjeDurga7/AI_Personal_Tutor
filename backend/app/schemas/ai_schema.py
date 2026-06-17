from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
class SummaryRequest(BaseModel):
    notes: str
class FlashcardRequest(BaseModel):
    notes: str
class QuizRequest(BaseModel):
    notes: str
class StudyPlanRequest(BaseModel):
    goal: str