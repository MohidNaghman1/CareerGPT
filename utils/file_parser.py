# utils/file_parser.py
import os
import fitz
import docx

def extract_text_from_file(file_path: str) -> str:
    """Extracts text from a PDF or DOCX file."""
    if not os.path.exists(file_path):
        return "Error: File not found."
    
    if file_path.lower().endswith('.pdf'):
        try:
            with fitz.open(file_path) as doc:
                text = "".join(page.get_text() for page in doc)
                if not text.strip():
                    return "Error: No text could be extracted from this PDF. It is likely an image-only file (a scan)."
                return text
        except Exception as e:
            return f"Error reading PDF: {e}"
            
    elif file_path.lower().endswith('.docx'):
        try:
            doc = docx.Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            return f"Error reading DOCX: {e}"
            
    else:
        return "Error: Unsupported file type."