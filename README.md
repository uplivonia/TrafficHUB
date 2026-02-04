# Trafik Hub — project skeleton

A monorepo starter for a "traffic hub" app that lets users connect multiple networks (Telegram/Discord/Reddit/X, etc.)
and orchestrate posting + engagement via a single dashboard.

## What’s inside
- **backend/** — FastAPI API server (integrations, flows, events)
- **worker/** — background job worker (Redis Queue) for scheduled/async actions
- **frontend/** — React + Vite UI (dashboard placeholder)
- **docker-compose.yml** — Postgres + Redis + backend + worker (frontend runs locally by default)

> This is a skeleton: connectors contain stubs and clear extension points.

## Quick start (Docker)
1) Copy env:
```bash
cp .env.example .env
```

2) Start infra + API + worker:
```bash
docker compose up --build
```

Backend will be on: http://localhost:8000  
Docs: http://localhost:8000/docs

## Frontend (local)
Requires Node 18+.
```bash
cd frontend
npm i
npm run dev
```
UI: http://localhost:5173

## How to add a new network connector
1) Create a folder in `backend/app/services/connectors/<network>/`
2) Implement the `Connector` interface from `backend/app/services/connectors/base.py`
3) Register it in `backend/app/services/connectors/registry.py`
4) Add API endpoints in `backend/app/api/v1/endpoints/integrations.py`

## Roadmap ideas
- OAuth + token vault
- visual flow builder (nodes/edges)
- analytics + rate limits + anti-ban safety
- templates marketplace
