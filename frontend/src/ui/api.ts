const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function getSupportedIntegrations() {
  const res = await fetch(`${API_URL}/api/v1/integrations/`);
  if (!res.ok) throw new Error("Failed to load integrations");
  return res.json();
}

export async function connectIntegration(network: string) {
  const res = await fetch(`${API_URL}/api/v1/integrations/connect`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ network, credentials: {} }),
  });
  if (!res.ok) throw new Error("Failed to connect");
  return res.json();
}
