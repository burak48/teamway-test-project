''' FastAPI main:app '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints.v1.url import api_router as api_v1_router
from config.base import API_V1_STR
from config.base import PROJECT_NAME

app = FastAPI(title=PROJECT_NAME, openapi_url=f"{API_V1_STR}/openapi.json")

# set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix=API_V1_STR)