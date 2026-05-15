# GRC Copilot — Full Tool

Complete GRC (Governance, Risk & Compliance) assessment platform with:
- **Frontend**: React 19 + Vite (port 5173)
- **Backend**: Node.js Express Gateway (port 3000)
- **Analysis Engine**: FastAPI Python (port 8000)
- **Databases**: PostgreSQL 16 + MongoDB 7

---

## What's Included

```
full-tool/
├── backend/
│   ├── node-gateway/      # Express API server
│   ├── fastapi-engine/    # Python analysis engine
│   └── docker-compose.yml # Database orchestration
├── frontend/              # React SPA
├── docker-compose.yml     # Full stack Docker setup
├── setup.sh / setup.bat   # Dependency installer
├── start.sh / start.bat   # One-click launcher
└── README.md             # This file
```

---

## Quick Start (Recommended)

### Option 1: Docker Compose (Easiest)

```bash
# 1. Start everything with Docker
docker-compose up -d

# 2. Open browser
http://localhost:5173
```

This starts:
- PostgreSQL on port 5432
- MongoDB on port 27017
- Node Gateway on port 3000
- FastAPI Engine on port 8000
- Frontend on port 5173

### Option 2: Manual Setup

#### Prerequisites
- Node.js 20+
- Python 3.12+
- Docker + Docker Compose

#### Step 1: Run Setup Script

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```cmd
setup.bat
```

This installs all npm and pip dependencies.

#### Step 2: Start Databases

```bash
docker-compose up -d postgres mongodb
```

#### Step 3: Start Application

**Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

**Windows:**
```cmd
start.bat
```

This opens 3 terminal windows and starts all services.

#### Step 4: Open Browser

Navigate to: **http://localhost:5173**

---

## Default Login

After registration, you can create your own account. No default credentials are set.

---

## API Endpoints

| Service | URL | Health Check |
|---------|-----|--------------|
| Frontend | http://localhost:5173 | - |
| Node Gateway | http://localhost:3000 | GET /health |
| FastAPI | http://localhost:8000 | GET /health |
| PostgreSQL | localhost:5432 | - |
| MongoDB | localhost:27017 | - |

---

## Features

### Assessment Types
- **Full Assessment**: Comprehensive audit of all controls
- **Quick Assessment**: 10-15 minute high-level check
- **Gap Assessment**: Identify control deficiencies
- **Risk Assessment**: Likelihood/impact scoring
- **Internal Audit**: Self-assessment for external readiness
- **Vendor Assessment**: Third-party security evaluation
- **AI Compliance Agent**: Auto-extract controls from policy documents

### Frameworks Supported
- ISO/IEC 27001:2022
- GDPR
- DPDPA (India)
- HIPAA Security Rule
- PCI DSS v4.0
- SOC 2 Trust Services Criteria
- NIST CSF 2.0
- CIS Controls v8

### Report Features
- CISO-ready PDF reports
- Domain maturity radar charts
- Risk heat maps
- Gap analysis tables
- Financial cost estimation (INR)
- Prioritized remediation roadmaps

---

## Architecture

```
┌─────────────────────────────────────────┐
│           Frontend (React)              │
│            http://localhost:5173        │
└─────────────────┬───────────────────────┘
                  │ API calls
┌─────────────────▼───────────────────────┐
│        Node Gateway (Express)           │
│            http://localhost:3000        │
│  Auth │ Org │ Questionnaire │ Dashboard │
└─────────────────┬───────────────────────┘
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
┌─────────┐ ┌──────────┐ ┌──────────┐
│PostgreSQL│ │ MongoDB  │ │ FastAPI  │
│  :5432   │ │  :27017  │ │  :8000   │
└─────────┘ └──────────┘ └──────────┘
```

---

## Environment Variables

### Backend (.env)
```env
NODE_ENV=development
PORT=3000
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=grc_copilot
POSTGRES_USER=grc_user
POSTGRES_PASSWORD=grc_secure_password_2025
MONGO_URI=mongodb://localhost:27017/grc_copilot
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
CORS_ORIGIN=http://localhost:5173
FASTAPI_URL=http://localhost:8000
```

### FastAPI (.env)
```env
DATABASE_URL=postgresql://grc_user:grc_secure_password_2025@localhost:5432/grc_copilot
MONGO_URI=mongodb://localhost:27017/grc_copilot
```

---

## Stopping Services

**Docker:**
```bash
docker-compose down
```

**Manual:**
- Press `Ctrl+C` in each terminal window
- Or close the terminal windows

---

## Troubleshooting

### Port Already in Use
```bash
# Find and kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Or for all GRC ports
for port in 3000 8000 5173 5432 27017; do
  lsof -ti:$port | xargs kill -9 2>/dev/null
done
```

### Database Connection Issues
```bash
# Restart databases
docker-compose down
docker-compose up -d postgres mongodb
```

### Frontend Shows "API Error 502"
The backend is not running. Start it with:
```bash
cd backend/node-gateway && npm start
```

---

## Sharing with Friends

1. Zip the `full-tool/` folder
2. Send the zip file
3. Friend extracts and runs:
   ```bash
   ./setup.sh   # or setup.bat on Windows
   ./start.sh   # or start.bat on Windows
   ```
4. Open http://localhost:5173

**Note**: Do NOT include `node_modules/` or `venv/` when sharing. The setup script installs these automatically.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19, Vite 8, React Router 7 |
| Backend | Node.js 20, Express 4, JWT |
| Analysis | Python 3.12, FastAPI, Uvicorn |
| Database | PostgreSQL 16, MongoDB 7 |
| AI | OpenAI/DeepSeek API integration |
| Reports | ReportLab (PDF), python-docx |

---

## License

MIT License — Free for personal and commercial use.

---

**Built with ❤️ for compliance professionals.**
