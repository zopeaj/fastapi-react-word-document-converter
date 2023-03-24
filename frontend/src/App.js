import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ConvertCorelDrawToPdf from "./views/ConvertCorelDrawToPdf";
import ConvertExcelToPdf from "./views/ConvertExcelToPdf";
import ConvertPdfToExcel from "./views/ConvertPdfToExcel";
import ConvertPdfToWord from "./views/ConvertPdfToWord";
import ConvertWordToPdf from "./views/ConvertWordToPdf";


function App() {
  return (
     <BrowserRouter>
       <Routes>
         <Route path="/" element={<Main />}>
           <Route path='convert-core-draw-to-pdf' element={<ConvertCorelDrawToPdf />}  />
           <Route path='convert-excel-to-pdf' element={<ConvertExceToPdf/>} />
           <Route path='convert-pdf-to-excel' element={<ConvertPdfToExcel/>} />
           <Route path='convert-pdf-to-word' element={<ConvertPdfToWord />} />
           <Route path='convert-word-to-pdf' element={<ConvertWordToPdf/>} />
           <Route path="*" element={<ErrorPage />} />
         </Route>
       </Routes>
     </BrowserRouter>
  );
}

export default App;
