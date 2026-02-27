# tools.py

import os
from langchain_community.document_loaders import PyPDFLoader

# ============================
# PDF Reader
# ============================

def read_pdf_text(file_path: str, max_pages: int = 3) -> str:
    """
    Reads limited pages from a PDF to avoid token overflow.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    cleaned = []

    for page in docs[:max_pages]:
        text = page.page_content.strip()
        text = " ".join(text.split())
        cleaned.append(text)

    return "\n".join(cleaned)