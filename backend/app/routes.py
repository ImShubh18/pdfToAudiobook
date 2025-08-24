from fastapi import APIRouter, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
import os
import PyPDF2
from gtts import gTTS

# Assuming these are in your services and utils directories
# Make sure to create these files if they don't exist
# from .services.pdf_service import extract_text
# from .services.audio_service import text_to_audio
# from .utils.file_utils import save_upload

router = APIRouter()

# Directories should be defined in a config or main.py for a cleaner structure
UPLOAD_DIR = "uploads"
AUDIO_DIR = "audio"

@router.post("/convert")
async def convert(
    file: UploadFile,
    start_page: int = Form(...),
    end_page: int = Form(...),
    gender: str = Form(...),
    speed: int = Form(...),
):
    try:
        # Save uploaded PDF
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text from PDF pages
        text = ""
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(reader.pages)
            start = max(start_page - 1, 0)
            end = min(end_page, total_pages)
            for i in range(start, end):
                text += reader.pages[i].extract_text() or ""

        if not text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in PDF in the selected pages.")

        # Convert text to speech
        tld = "com" if gender == "male" else "co.uk"
        tts = gTTS(text=text, lang="en", tld=tld, slow=(speed < 100))
        audio_filename = os.path.splitext(file.filename)[0] + ".mp3"
        audio_path = os.path.join(AUDIO_DIR, audio_filename)
        tts.save(audio_path)

        return FileResponse(audio_path, media_type="audio/mpeg", filename=audio_filename)

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during conversion.")