import shutil
from typing import List, Any


class DocumentConverterService:
    def __init__(self):
        self.maximum_file_size = 1024 * 1024

    def convertWordToPdf(self, files: List[Any]):
        file_data = None
        if len(files) == 1:
            file_data = files[0]
            if not file_data.filename.endswith('.docx'):
                return None

            if not self.check_file_size(file):
                return None

            with open(file_data.filename, mode='rb') as rf:
                contents = rf.read()
            filename = f'{file_data.filename}.pdf'
            with open(filename, mode='wb') as wf:
                wf.write(contents)
            return filename
        else:
            for file in files:
                if not file.filename.endswith('.docx'):
                    return None

                if not self.check_file_size(file):
                    return None
                else:
                    filename_list = []
                    with open(file.filename, mode='rb') as rf:
                        contents = rf.read()
                    filename = f'{file.filename}.pdf'
                    with open(filename, mode='wb') as wf:
                        wf.write(contents)
                    filename_list.append(filename)
                    return filename_list

    def convertPdfToWord(self, files: List[Any]):
        file_data = None
        if len(files) == 1:
            file_data = files[0]
            if not file_data.filename.endswith('.pdf'):
                return None

            if not self.check_file_size(file):
                return None

            with open(file_data.filename, mode='rb') as rf:
                contents = rf.read()
            filename = f'{file_data.filename}.docx'
            with open(filename, mode='wb') as wf:
                wf.write(contents)
            return filename
        else:
            for file in files:
                if not file.filename.endswith('.pdf'):
                    return None

                if not self.check_file_size(file):
                    return None

                filename_list = []
                with open(file.filename, mode='rb') as rf:
                    contents = rf.read()
                filename = f'{file.filename}.docx'
                with open(filename, mode='wb') as wf:
                    wr.write(contents)
                    filename_list.append(filename)
                return filename_list

    def convertExcelToPdf(self, files: List[Any]):
        file_data = None
        if len(files) == 1:
            file_data = files[0]

            if not file_data.filename.endswith('.xsxl'):
                return None

            if not self.check_file_size(file):
                return None

            with open(file_data.filename, mode='rb') as rf:
                contents = rf.read()
            filename = f'{file_data.filename}.pdf'
            with open(filename, mode='wb') as wf:
                wf.write(contents)
            return filename
        else:
            for file in files:
                if not file.filename.endswith('.xsxl'):
                    return None

                if not self.check_file_size(file):
                    return None

                filename_list = []
                with open(file.filename, mode='rb') as rf:
                    contents = rf.read()
                filename = f'{file.filename}.pdf'
                with open(filename, mode='wb') as wf:
                    wf.write(contents)
                    filename_list.append(filename)
                return filename_list

    def convertPdfToExcel(self, files: List[Any]):
        file_data = None
        if len(files) == 1:
            file_data = files[0]
            if not file_data.filename.endswith('.pdf'):
                return None

            if not self.check_file_size(file):
                return None

            with open(file_data.filename, mode='rb') as rf:
                contents = rf.read()
            filename = f'{file_data.filename}.xsxl'
            with open(filename, mode='wb') as wf:
                wf.write(contents)
            return filename
        else:
            for file in files:
                if not file.filename.endswith('.pdf'):
                    return None

                if not self.check_file_size(file):
                    return None
                filename_list = []
                with open(file.filename, mode='rb') as rf:
                    contents = rf.read()
                filename = f'{file.filename}.xsxl'
                with open(filename, mode='wb') as wf:
                    wf.write(contents)
                    filename_list.append(filename)
                return filename_list

    def convertCorelDrawToPdf(self, files: List[Any]):
        file_data = None
        if len(files) == 1:
            file_data = files[0]
            if not file_data.filename.endswith('.crldraw'):
                return None

            if not self.check_file_size(file):
                return None

            with open(file_data.filename, mode='rb') as rf:
                contents = rf.read()
            filename = f'{file_data.filename}.pdf'
            with open(filename, mode='wb') as wf:
                wf.write(contents)
            return filename
        else:
            for file in files:
                if not file.filename.endswith('.crldraw'):
                    return None

                if not self.check_file_size(file):
                    return None

                filename_list = []
                with open(file.filename, mode='rb') as rf:
                    contents = rf.read()
                filename = f'{file.filename}.pdf'
                with open(filename, mode='wb') as wf:
                    wf.write(contents)
                    filename_list.append(filename)
                return filename_list

    def check_file_size(self, file):
        return self.get_maximum_file_size() == len(file)

    def get_maximum_file_size(self):
        return self.maximum_file_size

    def write_file_data_content(self, file):
        try:
            with open(file.filename, 'wb') as f:
                while contents := file.file.read(self.get_maximum_file_size()):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()

        return {"message": f"Successfully uploaded {file.filename}"}


    def copy_pdf_document_to_word_document(self, file):
        try:
            with open(file.filename, 'wb') as f:
                shutil.copyfileobj(file.file, f)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()

        return {"message": f"Successfully uploaded {file.filename}"}

    def convert_multiple_pdf_to_word(self, files: List[Any]):
        for file in files:
            try:
                contents = file.file.read()
                with open(f'{file.filename}.docx', 'wb') as f:
                    f.write(contents)
            except Exception:
                return None or {"message": "There was an error uploading the file"}
            finally:
                file.file.close()

        return {"message": f"Successfully uploaded {[file.filename for file in files]}"}

    def convert_multiple_word_to_pdf(self, files: List[Any]):
        for file in files:
            try:
                if(file.filename.endswith('.docx')):
                    contents = file.file.read()
                    with open(f'{file.filename}.pdf', 'wb') as f:
                        f.write(contents)
                else:
                    return None
            except Exception:
                return {"message": "There was an error uploading the file(s)"}
            finally:
                file.file.close()
        return {"message": f"Successfully uploaded {[file.filename for file in files]}"}


