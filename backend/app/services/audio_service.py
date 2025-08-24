import pyttsx3
import os

TEMP_DIR = "backend/temp"

def text_to_audio(text: str, gender: str, speed: int) -> str:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    if gender.lower() == "female":
        for v in voices:
            if "female" in v.name.lower():
                engine.setProperty("voice", v.id)
                break
    else:
        for v in voices:
            if "male" in v.name.lower():
                engine.setProperty("voice", v.id)
                break

    engine.setProperty("rate", speed)
    output_path = os.path.join(TEMP_DIR, "audiobook.mp3")
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path
