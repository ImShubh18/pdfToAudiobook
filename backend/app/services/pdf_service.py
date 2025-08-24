import fitz

def extract_text(pdf_path: str, start_page: int, end_page: int) -> str:
    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    if start_page < 1 or start_page > total_pages or end_page > total_pages or start_page > end_page:
        raise ValueError("Invalid page range")

    return "\n".join([doc[i].get_text() for i in range(start_page-1, end_page)]).strip()
