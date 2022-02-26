''' Mock API of /api/v1/questions '''

from fastapi import APIRouter
from fastapi import Response
from fastapi import Query

import os.path
import json

router = APIRouter()


@router.get("/questions")
def questions(response: Response, question_id: str = Query(..., min_length=1)):
    '''
        Serves the questions that have been saved
        Args:
            question_id (str): ID property of the question

        Returns:
            FastAPI JsonResponse
    '''

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, '..', '..', '..', 'data', 'questions.json')
    with open(path) as f:
        data = json.load(f)

    if question_id == "1":
        result = data.get("questions_v1")
    elif question_id == "2":
        result = data.get("questions_v2")
    elif question_id == "3":
        result = data.get("questions_v3")
    elif question_id == "4":
        return Response(content=None, status_code=204)
    elif question_id == "5":
        return Response(content=None, status_code=400)
    elif question_id == "6":
        return Response(content=None, status_code=500)

    if result:
        response = result

    return response
