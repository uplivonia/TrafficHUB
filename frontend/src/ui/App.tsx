import React from "react";
import { getSupportedIntegrations, connectIntegration } from "./api";

export default function App() {
  const [supported, setSupported] = React.useState<string[]>([]);
  const [log, setLog] = React.useState<string>("");

  React.useEffect(() => {
    getSupportedIntegrations()
      .then((d) => setSupported(d.supported || []))
      .catch((e) => setLog(String(e)));
  }, []);

  async function onConnect(network: string) {
    setLog("connecting...");
    try {
      const r = await connectIntegration(network);
      setLog(JSON.stringify(r, null, 2));
    } catch (e) {
      setLog(String(e));
    }
  }

  return (
    <div style={{ maxWidth: 980, margin: "0 auto", padding: 18 }} className="grid">
      <div className="card">
        <div style={{ fontSize: 22, fontWeight: 700 }}>Trafik Hub</div>
        <div className="small">
          One dashboard to orchestrate bots + content across networks (skeleton UI).
        </div>
      </div>

      <div className="card grid">
        <div style={{ fontSize: 16, fontWeight: 600 }}>Supported integrations</div>
        <div className="row">
          {supported.map((n) => (
            <button key={n} className="btn" onClick={() => onConnect(n)}>
              Connect {n}
            </button>
          ))}
        </div>
        <div className="small">Next: add OAuth/token storage + real connector implementations.</div>
      </div>

      <div className="card">
        <div style={{ fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Log</div>
        <pre style={{ whiteSpace: "pre-wrap", margin: 0 }}>{log}</pre>
      </div>
    </div>
  );
}
