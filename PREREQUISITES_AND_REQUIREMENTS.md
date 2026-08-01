# 📦 Velixo: System Requirements & Setup Guide

This document outlines all technical requirements, software prerequisites, installation instructions, and deployment steps to run and scale **Velixo (AI Work Operating System)**.

---

## 💻 1. System Requirements & Prerequisites

| Requirement | Minimum Version | Recommended Version | Status / Notes |
| :--- | :--- | :--- | :--- |
| **Operating System** | Windows 10/11, macOS 12+, Linux | Windows 11 / macOS | Supported on all OS |
| **Python** | Python 3.9+ | Python 3.11 / 3.12 | Required for FastAPI backend |
| **Node.js** | Node v18.0.0+ | Node v22.0.0+ | Required for React/Vite frontend |
| **npm** | npm v8.0.0+ | npm v10.0.0+ | Package manager for frontend |
| **RAM** | 4 GB | 8 GB+ | For local LLM & multi-agent execution |
| **Disk Space** | 500 MB | 2 GB | Dependencies & local vector store |

---

## 🛠️ 2. Step-by-Step Setup & Installation

### Step A: Clone & Open Repository
```bash
cd c:\Users\parth\OneDrive\Desktop\Velixo
```

### Step B: Backend Python Setup
```bash
# 1. Navigate to backend directory
cd backend

# 2. (Optional) Create Python virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install Python backend dependencies
pip install -r requirements.txt
```

### Step C: Frontend React Setup
```bash
# 1. Navigate to client directory
cd ../client

# 2. Install frontend npm dependencies
npm install
```

---

## ⚡ 3. Running Velixo

### Single Command Launcher (Recommended)
From the root workspace directory, run:
```bash
python start_velixo.py
```
*(Or double-click `run_app.bat` on Windows)*

This single launcher script automatically starts:
* **FastAPI AI Engine Backend**: `http://localhost:8000` (API Docs at `http://localhost:8000/docs`)
* **React Glassmorphic Dashboard**: `http://localhost:5173`

---

## ☁️ 4. Deployment Instructions (Production Ready)

### Deploying Frontend to Vercel
1. Push workspace to GitHub repository.
2. Go to [Vercel Dashboard](https://vercel.com/) and import the repository.
3. Set **Root Directory** to `client`.
4. Set Build Command to `npx vite build` and Output Directory to `dist`.
5. Deploy!

### Deploying Backend to Render / Railway / Cloud Run
1. Create a new Web Service on [Render](https://render.com/) or [Railway](https://railway.app/).
2. Set **Root Directory** to `backend`.
3. Set Start Command to `python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
4. Add environment variables (`GEMINI_API_KEY`, etc.).
5. Deploy!
