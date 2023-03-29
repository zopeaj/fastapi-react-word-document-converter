import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter, Request, File, UploadFile, Depends
from app.core.business.abstracts.DocumentConverterService import DocumentConverterService
from fastapi.responses import FileResponse

documentConverterService = DocumentConverterService()
documentroutes = APIRouter()

@documentroutes.post("/convert-word-to-pdf")
def convert_word_to_pdf(request: Request, files: List[UploadFile] = File(...)) -> FileResponse:
    return documentConverterService.convertWordToPdf(files)

@documentroutes.post("/convert-pdf-to-word")
def convert_pdf_to_word(request: Request, files: List[UploadFile] = File(...)) -> FileResponse:
    return documentConverterService.convertPdfToWord(files)

@documentroutes.post("/convert-corel-draw-to-pdf")
def convert_corel_draw_to_pdf(request: Request, files: List[UploadFile] = File(...)) -> FileResponse:
    return documentConverterService.convertCorelDrawToPdf(files)

@documentroutes.post("/convert-excel-to-pdf")
def convert_excel_to_pdf(request: Request, files: List[UploadFile] = File(...)) -> FileResponse:
    return documentConverterService.convertExcelToPdf(files)

@documentroutes.post("/convert-pdf-to-excel")
def convert_pdf_to_excel(request: Request, files: List[UploadFile] = File(...)) -> FileResponse:
    return documentConverterService.convertPdfToExcel(files)


