import pdfplumber
from ocr_resume_extractor import ocr_extract_text_from_pdf

def try_pdfplumber_extraction(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def extract_resume_text(pdf_path):
    # Try normal extraction first
    text = try_pdfplumber_extraction(pdf_path)
    if len(text.strip()) == 0:
        print("Using OCR for text extraction...")
        text = ocr_extract_text_from_pdf(pdf_path)
    return text

