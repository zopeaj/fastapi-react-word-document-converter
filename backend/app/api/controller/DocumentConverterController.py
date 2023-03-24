import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter, Request
from app.core.business.abstracts.DocumentConverterService import DocumentConverterService
from fastapi.responses import FileResponse

documentConverterService = DocumentConverterService()
documentroutes = APIRouter()

@documentroutes.post("/convert-word-to-pdf")
def convert_word_to_pdf(request: Request) -> FileResponse:
    pass

@documentroutes.post("/convert-pdf-to-word")
def convert_pdf_to_word(request: Request) -> FileResponse:
    pass

@documentroutes.post("/convert-corel-draw-to-pdf")
def convert_corel_draw_to_pdf(request: Request) -> FileResponse:
    pass

@documentroutes.post("/convert-excel-to-pdf")
def convert_excel_to_pdf(request: Request) -> FileResponse:
    pass

@documentroutes.post("/convert-pdf-to-excel")
def convert_pdf_to_excel(request: Request) -> FileResponse:
    pass


