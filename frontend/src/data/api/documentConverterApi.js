import { API_URL } from "../../env";

const checkStatus = (response) => {
  if(response.ok) {
    return response;
  }
  const error = new Error(response.statusText);
  error.response = response;
  return error;
}

export const convertWordToPdf = async (data) => {
  return await fetch(API_URL + 'convert-word-to-pdf', {
    method: "POST",
    headers: {
      "Content-Type": "multipart/form-data"
    },
    body: data
  }).then(checkStatus)
}

export const convertPdfToWord = async (data) => {
  return await fetch(API_URL + 'convert-pdf-to-word', {
    method: "POST",
    headers: {
      "Content-Type": "multipart/form-data"
    },
    body: data
  }).then(checkStatus)
}

export const convertExcelToPdf = async (data) => {
  return await fetch(API_URL + 'convert-excel-to-pdf', {
    method: "POST",
    headers: {
      "Content-Type": "multipart/form-data"
    },
    body: data
  }).then(checkStatus)
}

export const convertPdfToExcel = async(data) => {
  return await fetch(API_URL + 'convert-pdf-to-excel', {
    method: "POST",
    headers: {
      "Content-Type": "multipart/form-data"
    },
    body: data
  }).then(checkStatus)
}

export const convertCorelDrawToPdf = async (data) => {
  return await fetch(API_URL + 'convert-corel-draw-to-pdf', {
    method: "POST",
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(checkStatus)
}


