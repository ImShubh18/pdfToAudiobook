import React from "react";

const AudioPlayer = ({ audioUrl }) => {
  if (!audioUrl) return null;
  return (
    <div>
      <h3>Generated Audiobook</h3>
      <audio controls src={audioUrl}></audio>
    </div>
  );
};

export default AudioPlayer;
