import pytesseract
from pdf2image import convert_from_path

def extract_text_from_image(file_path):
    return pytesseract.image_to_string(file_path)

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for p in pages:
        text += pytesseract.image_to_string(p)
    return text

