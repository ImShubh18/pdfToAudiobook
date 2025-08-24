import React, { useState } from "react";
import axios from "axios";

const PdfUpload = ({ setAudioUrl }) => {
  const [file, setFile] = useState(null);
  const [startPage, setStartPage] = useState(1);
  const [endPage, setEndPage] = useState(1);
  const [gender, setGender] = useState("female");
  const [speed, setSpeed] = useState(150);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);
    formData.append("start_page", startPage);
    formData.append("end_page", endPage);
    formData.append("gender", gender);
    formData.append("speed", speed);

    const response = await axios.post("http://localhost:8000/convert", formData, {
      responseType: "blob",
    });

    const url = URL.createObjectURL(response.data);
    setAudioUrl(url);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept="application/pdf" onChange={(e) => setFile(e.target.files[0])} required />
      <input type="number" value={startPage} onChange={(e) => setStartPage(e.target.value)} />
      <input type="number" value={endPage} onChange={(e) => setEndPage(e.target.value)} />
      <select value={gender} onChange={(e) => setGender(e.target.value)}>
        <option value="male">Male</option>
        <option value="female">Female</option>
      </select>
      <input type="number" value={speed} onChange={(e) => setSpeed(e.target.value)} />
      <button type="submit">Convert</button>
    </form>
  );
};

export default PdfUpload;
