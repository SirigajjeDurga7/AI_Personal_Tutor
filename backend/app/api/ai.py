from fastapi import APIRouter
from app.schemas.ai_schema import ChatRequest
from app.ai.tutor import ask_ai
from app.schemas.ai_schema import SummaryRequest
from app.ai.summarizer import summarize_notes
from app.schemas.ai_schema import FlashcardRequest
from app.ai.flashcards import generate_flashcards
from app.schemas.ai_schema import QuizRequest
from app.ai.quiz_generator import generate_quiz
from app.schemas.ai_schema import StudyPlanRequest
from app.ai.study_planner import generate_study_plan
router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/chat")
async def chat_with_ai(data: ChatRequest):

    answer = await ask_ai(data.question)

    return {
        "question": data.question,
        "answer": answer
    }
@router.post("/summarize")
async def summarize(data: SummaryRequest):

    summary = await summarize_notes(data.notes)

    return {
        "summary": summary
    }
@router.post("/flashcards")
async def flashcards(data: FlashcardRequest):

    cards = await generate_flashcards(data.notes)

    return {
        "flashcards": cards
    }
@router.post("/quiz")
async def quiz(data: QuizRequest):

    quiz_data = await generate_quiz(data.notes)

    return {
        "quiz": quiz_data
    }
@router.post("/study-plan")
async def study_plan(data: StudyPlanRequest):

    plan = await generate_study_plan(data.goal)

    return {
        "study_plan": plan
    }