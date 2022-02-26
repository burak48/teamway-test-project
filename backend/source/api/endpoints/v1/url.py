''' API File '''

from fastapi import APIRouter
from .questions import router as questions

api_router = APIRouter()
api_router.include_router(questions)
