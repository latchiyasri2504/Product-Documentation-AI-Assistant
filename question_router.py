from fastapi import APIRouter, HTTPException
from src.schemas import QuestionRequest, AnswerResponse
from src.services.inference_service import generate_answer

router = APIRouter()


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    try:
        answer = generate_answer(request.question)

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to process your question"
        )