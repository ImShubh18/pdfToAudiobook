from backend.app.services.pdf_service import extract_text

def test_extract_text():
    sample_pdf = "backend/tests/sample.pdf"  # add a dummy pdf
    text = extract_text(sample_pdf, 1, 1)
    assert isinstance(text, str)
