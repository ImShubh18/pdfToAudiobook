from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from .routes import router

app = FastAPI()

# CORS for React frontend
origins = [
    "http://localhost:3000",
    "http://localhost:5173", # Add this if your frontend is running on a different port
    "http://127.0.0.1:5173",  # Include this as well for full compatibility
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Use the list here
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(router)

# Create necessary directories
UPLOAD_DIR = "uploads"
AUDIO_DIR = "audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)