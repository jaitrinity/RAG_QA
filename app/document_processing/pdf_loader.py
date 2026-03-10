import fitz

def extract_text_from_pdf(file_path):

    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()
    
    # print(f"Extracted text length: {len(text)}")
    # print(f"Extracted text: {text}")
    return text