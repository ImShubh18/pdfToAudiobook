📖🎧 PDF to Audiobook Converter

Turn your PDFs into audiobooks effortlessly!
This full-stack web application lets users upload a PDF, choose page ranges, customize voice & speed, and generate a downloadable MP3 audiobook with real-time playback.

✨ Features

✅ PDF Upload – Easily upload PDF files.
✅ Customizable Conversion – Select specific pages or the entire document.
✅ Voice Customization – Choose between 🎙️ male or 🎙️ female voices + adjust speaking speed.
✅ Real-time Playback – Preview audio in the browser before downloading.
✅ Responsive UI – Clean and simple design for a smooth user experience.

🛠️ Tech Stack
🎨 Frontend

⚛️ React – Component-based UI

🌐 Axios – API requests

⚡ Backend

🚀 FastAPI – High-performance Python web framework

📄 PyPDF2 – Extract text from PDFs

🔊 gTTS (Google TTS) – Convert text into speech

⚡ Uvicorn – ASGI server

⚙️ Installation & Setup
🔹 Prerequisites

Python 3.8+

Node.js + npm

🔹 Backend Setup
cd backend
python -m venv venv
# Activate venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload


👉 Backend runs at: http://127.0.0.1:8000

🔹 Frontend Setup
cd frontend
npm install
npm run dev


👉 Frontend runs at: http://localhost:5173

👨‍💻 Usage

Run both backend & frontend servers.

Open 👉 http://localhost:5173 in your browser.

Upload a PDF file.

Select page range, voice gender, and speed.

Click Convert 🎉

🎧 Preview audio → 💾 Download MP3.

📌 Demo Flow

Upload PDF →

Set Options →

Convert →

Listen in Browser / Download

🚀 Future Enhancements

🌍 Multi-language TTS support

🎵 Background music option

📱 Mobile app version
