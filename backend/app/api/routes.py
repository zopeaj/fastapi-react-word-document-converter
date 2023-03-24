import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from app.api.controller.DocumentConverterController import documentroutes

api_router = APIRouter()
api_router.include_router(documentroutes, prefix="", tags=['document-converter'])
