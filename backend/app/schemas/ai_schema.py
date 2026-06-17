from pydantic import BaseModel
from typing import List

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
class CareerRequest(BaseModel):
    skills: List[str]
    interest: str

class RecommendationRequest(BaseModel):
    weak_topics: List[str]

class InterviewRequest(BaseModel):
    domain: str