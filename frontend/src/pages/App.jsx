import React, { useState } from "react";
import axios from "axios";
import "./App.css";
export default function App() {
  const [file, setFile] = useState(null);
  const [audioUrl, setAudioUrl] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please upload a PDF file!");
    // Corrected logic for App.jsx (or use PdfUpload.jsx which already has this logic)
    const formData = new FormData();
    formData.append("file", file);
    formData.append("start_page", 1); // Example hardcoded value
    formData.append("end_page", 1); // Example hardcoded value
    formData.append("gender", "female"); // Example hardcoded value
    formData.append("speed", 150); // Example hardcoded value

    try {
      setLoading(true);
      const res = await axios.post(
        "http://127.0.0.1:8000/convert",
        formData,
        { responseType: "blob" } // keep this to get the audio
      );

      const url = URL.createObjectURL(res.data);
      setAudioUrl(url);
    } catch (err) {
      console.error(err);
      alert("Upload failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>📖 PDF to Audiobook</h1>
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button
        onClick={handleUpload}
        disabled={loading}
        style={{ marginLeft: "10px" }}
      >
        {loading ? "Processing..." : "Convert to Audio"}
      </button>

      {audioUrl && (
        <div style={{ marginTop: "20px" }}>
          <h2>🎧 Listen</h2>
          <audio controls src={audioUrl}></audio>
        </div>
      )}
    </div>
  );
}
