PDF to Audiobook Converter 📖🎧

This is a full-stack web application that converts PDF documents into an audiobook format. Users can upload a PDF, select a page range, and customize the audio output (gender and speed) to create a downloadable MP3 file.

🚀 Features
PDF Upload: Easily upload PDF files to the application.

Customizable Conversion: Specify a range of pages to convert, from a single page to the entire document.

Voice Customization: Adjust the text-to-speech voice by choosing between male and female tones and setting a custom speaking speed.

Real-time Playback: Listen to the generated audiobook directly in the browser before downloading it.

Simple Interface: The application features a clean, intuitive, and responsive user interface.

🛠️ Technology Stack
Frontend
React: Used for building the user interface and managing component state.

Axios: A library for handling API requests from the frontend to the backend.

Backend
FastAPI: A modern, high-performance web framework for the API, built with Python.

PyPDF2: A Python library for extracting text from PDF documents.

gTTS (Google Text-to-Speech): A Python library that converts text into audio using Google's TTS API.

Uvicorn: An ASGI server to serve the FastAPI application.

⚙️ Installation & Setup
Prerequisites
Make sure you have Python 3.8+ and Node.js with npm installed on your system.

Backend
Navigate to the backend directory.

Bash

cd backend
Create and activate a virtual environment to manage dependencies.

Bash

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install the required Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
Run the backend server.

Bash

uvicorn main:app --reload
The server will be available at http://127.0.0.1:8000.

Frontend
Open a new terminal and go to the frontend directory.

Bash

cd frontend
Install the necessary npm packages.

Bash

npm install
Start the React development server.

Bash

npm run dev
The frontend application will run on http://localhost:5173.

👨‍💻 Usage
Ensure both the backend and frontend servers are running.

Open your web browser and go to http://localhost:5173.

Use the form to upload a PDF file from your computer.

Set your desired page range, voice gender, and speed.

Click the "Convert" button. Once the conversion is complete, an audio player will appear, allowing you to listen to your new audiobook.






