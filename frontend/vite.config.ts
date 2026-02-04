import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    base: "/TrafficHUB/",
    plugins: [react()],
    server: { port: 5173 },
});
