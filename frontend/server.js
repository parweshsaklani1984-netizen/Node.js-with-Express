const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;
const backendUrl = process.env.BACKEND_URL || 'http://localhost:5000/process';

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/submit', async (req, res) => {
  try {
    const backendResponse = await fetch(backendUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(req.body)
    });

    const result = await backendResponse.json();
    res.status(backendResponse.status).json(result);
  } catch (error) {
    console.error('Backend request failed:', error.message);
    res.status(502).json({ error: 'The backend is unavailable. Please try again.' });
  }
});

app.listen(port, () => {
  console.log(`Frontend listening on port ${port}`);
});