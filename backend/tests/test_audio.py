from backend.app.services.audio_service import text_to_audio
import os

def test_text_to_audio():
    text = "Hello, this is a test."
    path = text_to_audio(text, gender="male", speed=150)
    assert os.path.exists(path)
