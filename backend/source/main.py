''' FastAPI main:app '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints.v1.url import api_router as api_v1_router

app = FastAPI()

# set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router)