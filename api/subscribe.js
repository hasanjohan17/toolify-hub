export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Content-Type', 'application/json');

  if (req.method === 'OPTIONS') return res.status(200).end();

  try {
    let email = req.body?.email;
    if (!email || typeof email !== 'string') {
      return res.status(400).json({ error: 'Email is required and must be a string' });
    }

    email = email.trim().toLowerCase();
    if (!email.includes('@')) {
      return res.status(400).json({ error: 'Invalid email format' });
    }

    const apiKey = process.env.BREVO_API_KEY;
    if (!apiKey) {
      console.error('BREVO_API_KEY is not set');
      return res.status(500).json({ error: 'API key not configured' });
    }

    console.log('Subscribing email:', email, 'with API key length:', apiKey.length);

    const response = await fetch('https://api.brevo.com/v3/contacts', {
      method: 'POST',
      headers: {
        'api-key': apiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email,
        listIds: [3],
        updateEnabled: true
      })
    });

    const data = await response.json();
    console.log('Brevo response:', response.status, data);

    if (!response.ok) {
      return res.status(response.status).json({
        error: data.message || 'Subscription failed',
        brevo_error: data
      });
    }

    return res.status(200).json({ success: true });
  } catch (error) {
    console.error('API error:', error);
    return res.status(500).json({ error: error.message });
  }
}
