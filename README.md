# Velixo: Next-Generation AI Work Operating System (AI Chief of Staff)

> **Tagline**: *"Your AI Chief of Staff for Work and Life. Think less. Achieve more."*

![Velixo Logo](client/public/logo.png)

Velixo is an autonomous, AI-native Work Operating System designed to replace traditional task managers. Instead of manually creating, prioritizing, and organizing tasks, Velixo acts as your personal Chief of Staff—handling Intent Management, Universal Multimodal Capture, Persistent AI Memory, Knowledge Graph relationship tracking, Autonomous Daily Planning, and Work-Life Analytics.

---

## ✨ Core Features

* **Intent Management Engine**: State your high-level goal (e.g., *"Launch product launch campaign next month"*); Velixo automatically breaks down tasks, assigns priorities, and schedules deep work.
* **Universal Multimodal Capture**: Drag and drop PDFs, voice notes, code snippets, emails, screenshots, or web links to instantly convert raw inputs into structured tasks.
* **Autonomous Daily Planner**: Dynamic schedule engine that blocks time for deep work based on energy levels, calendar events, and deadlines.
* **Work-Life Knowledge Graph**: Interactive visual node graph mapping connections across projects, tasks, skills, documents, and personal habits.
* **Multi-Provider AI Layer**: Modular LLM layer supporting Google Gemini API (Primary), Groq, OpenRouter, NVIDIA NIM, and local offline fallback options.
* **AI Chief of Staff Assistant**: Multi-turn chat interface with persistent memory of all past projects, meetings, and context.

---

## 🛠️ Project Structure

```text
Velixo/
├── backend/                  # FastAPI Python Backend (API & AI Layer)
│   ├── app/                  # FastAPI routers, models, AI providers, agents
│   ├── Dockerfile            # Container configuration for backend
│   └── requirements.txt      # Python dependencies
├── client/                   # React 19 + Vite Frontend Dashboard
│   ├── src/                  # React components, pages, state
│   ├── vercel.json           # Vercel SPA routing configuration
│   └── package.json          # Frontend dependencies
├── .env.example              # Environment variables template
├── .gitignore                # Root Git ignore rules
├── docker-compose.yml        # Docker orchestration file
├── start_velixo.py           # Unified local launcher (Backend + Frontend)
└── run_app.bat               # One-click Windows starter script
```

---

## 💻 Local Setup & Development

### Prerequisites
- **Python**: v3.9+ (Python 3.11/3.12 recommended)
- **Node.js**: v18.0+ & npm

### Quick Start (Single Command)
Run the master python script to start both backend and frontend concurrently:

```bash
python start_velixo.py
```
*(On Windows, you can double-click `run_app.bat`)*

- **Velixo Dashboard**: [http://localhost:5173](http://localhost:5173)
- **FastAPI Interactive Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📤 Step-by-Step Guide: Upload to GitHub

Follow these steps to initialize Git and push the repository to GitHub:

### 1. Initialize Git in the Project Root
Open your terminal in the root directory `Velixo/` and run:

```bash
git init
```

### 2. Stage & Commit Files
```bash
git add .
git commit -m "Initial commit: Velixo AI Work OS"
```

### 3. Link Remote Repository & Push to Main Branch
Create a new empty repository on [GitHub](https://github.com/new), then run:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```

---

## 🚀 Step-by-Step Guide: Deploy to Vercel

You can easily deploy the Velixo frontend to Vercel and backend to Render / Railway / Koyeb.

### Option A: Deploying Frontend via Vercel Dashboard (Recommended)

1. **Log in to Vercel**: Go to [Vercel](https://vercel.com/) and log in with your GitHub account.
2. **Import Project**:
   - Click **Add New...** -> **Project**.
   - Select your uploaded `YOUR_REPOSITORY_NAME` GitHub repository.
3. **Configure Project Settings**:
   - **Framework Preset**: `Vite`
   - **Root Directory**: Click *Edit* and select **`client`**
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. **Environment Variables**:
   - Add `VITE_API_URL` pointing to your deployed backend URL (e.g., `https://your-backend-service.onrender.com`).
5. **Deploy**: Click **Deploy**. Vercel will build and publish your frontend with live SPA routing enabled via `client/vercel.json`.

---

### Option B: Deploying Frontend via Vercel CLI

If you prefer using the command line:

```bash
# 1. Install Vercel CLI globally (if not already installed)
npm install -g vercel

# 2. Navigate to the client directory
cd client

# 3. Run Vercel deployment
vercel
```
Follow the interactive prompts to link and deploy your project.

---

### Deploying the FastAPI Backend

The backend can be hosted on any cloud provider supporting Python / Docker (e.g. Render, Railway, Koyeb, AWS App Runner).

#### Deploying on Render (Free / Web Service):
1. Create a **New Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Set **Root Directory**: `backend`
4. Set **Runtime**: `Python 3` (or Docker using `backend/Dockerfile`).
5. Set **Build Command**: `pip install -r requirements.txt`
6. Set **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
7. Add Environment Variables (from `.env.example`):
   - `DATABASE_URL` (Neon PostgreSQL URL)
   - `GEMINI_API_KEY`, `GROQ_API_KEY`, etc.

---

## 🔐 Environment Variables Reference

Copy `.env.example` to `.env` and fill in your keys:

```env
# AI Provider Keys
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
NVIDIA_NIM_API_KEY=your_nvidia_nim_api_key

# Database
DATABASE_URL=postgresql://user:password@host/neondb?sslmode=require

# App Config
PRIMARY_AI_PROVIDER=auto
PORT=8000
```

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more details.