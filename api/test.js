// Simple test endpoint to check if environment is configured
export default function handler(req, res) {
  const apiKey = process.env.BREVO_API_KEY;
  
  res.json({
    env_brevo_exists: !!apiKey,
    env_brevo_length: apiKey?.length,
    env_brevo_key: apiKey ? apiKey.substring(0, 20) + '...' : 'NOT SET',
    all_env_keys: Object.keys(process.env)
      .filter(k => k.toUpperCase().includes('BREVO') || k.toUpperCase().includes('API'))
      .map(k => k + ': ' + (process.env[k] ? '✓ set' : '✗ not set'))
  });
}
