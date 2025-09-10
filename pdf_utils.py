import PyPDF2

def extract_data_from_pdf(pdf_path: str) -> str:
    with open(pdf_path, "rb") as file:
        pdfreader = PyPDF2.PdfReader(file)
        full_text = ""
        for page in pdfreader.pages:
            full_text += page.extract_text()
    return full_text
