''' Mock API of /api/v1/questions '''

from fastapi import APIRouter
from fastapi import Response
from fastapi import Query

router = APIRouter()


@router.get("/questions/{question_id}")
def questions(response: Response, question_id: str = Query(..., min_length=1)):
    '''
        Serves the questions that have been saved
        Args:
            question_id (str): ID property of the question

        Returns:
            FastAPI JsonResponse
    '''

    return {"msg": "Hello, World!"}