import pytesseract
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_extract_text_from_pdf(pdf_path):
    poppler_path = r'C:\poppler-25.12.0\Library\bin'

    # Convert PDF pages to images, specifying poppler_path
    pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)

    text = ""
    for page_num, page in enumerate(pages):
        print(f"Processing page {page_num + 1}...")
        text += pytesseract.image_to_string(page) + "\n"

    return text

if __name__ == "__main__":
    pdf_file = "resumes/Resume.pdf"  # your scanned resume PDF path
    extracted_text = ocr_extract_text_from_pdf(pdf_file)
    print("Extracted Text Preview:\n", extracted_text[:1000])
