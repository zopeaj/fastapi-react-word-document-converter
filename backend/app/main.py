import os, sys
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, APIRouter
from app.api.routes import api_router

app = FastAPI(title="", openapi_url="")

app.include_router(api_router)
