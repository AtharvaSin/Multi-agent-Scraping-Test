import React from 'react';
import { useState } from 'react';

export default function App() {
  const [prompt, setPrompt] = useState('');
  const [status, setStatus] = useState('');
  const [items, setItems] = useState([]);

  const handleSubmit = async () => {
    setStatus('Running...');
    const res = await fetch('http://localhost:8000/run_job', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setStatus(`Completed: ${data.count} items scraped`);
    setItems(data.items || []);
  };

  return (
    <div className="container py-4">
      <h1 className="mb-4">Multi-Agent Scraper</h1>
      <div className="mb-3">
        <textarea className="form-control" rows="3" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      </div>
      <button className="btn btn-primary mb-3" onClick={handleSubmit}>Run</button>
      <p>{status}</p>
      {items.length > 0 && (
        <>
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Title</th>
                <th>Price</th>
              </tr>
            </thead>
            <tbody>
              {items.map((item, idx) => (
                <tr key={idx}>
                  <td>{item.title}</td>
                  <td>{item.price}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <a className="btn btn-secondary" href="http://localhost:8000/data_csv">Download CSV</a>
        </>
      )}
    </div>
  );
}
