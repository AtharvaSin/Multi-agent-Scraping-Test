import React from 'react';
import { useState } from 'react';

export default function App() {
  const [prompt, setPrompt] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async () => {
    setStatus('Running...');
    const res = await fetch('http://localhost:8000/run_job', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setStatus(`Completed: ${data.count} items scraped`);
  };

  return (
    <div>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      <button onClick={handleSubmit}>Run</button>
      <p>{status}</p>
    </div>
  );
}
