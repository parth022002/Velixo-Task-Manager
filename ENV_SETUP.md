# 📋 Velixo Master Environment Copy-Paste Guide

This file contains all environment variables formatted for quick copy-pasting to **Local `.env`**, **Vercel (Frontend)**, and **Render/Railway (Backend)**.

---

## 🟢 1. For Local Development (`.env` file)
Copy everything below into your `.env` file in the project root:

```env
# =====================================================================
# VELIXO LOCAL ENVIRONMENT CONFIGURATION (.env)
# =====================================================================

# 1. FRONTEND CONFIG
VITE_API_URL=http://localhost:8000
VITE_APP_FIREBASE_API_KEY=

# 2. DATABASE
DATABASE_URL=postgresql://neondb_owner:npg_ERJmtbgkO41Q@ep-solitary-shadow-az9g1d2n-pooler.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require

# 3. AI PROVIDER KEYS
GEMINI_API_KEY=
GROQ_API_KEY=
OPENROUTER_API_KEY=
NVIDIA_API_KEY=
OPENAI_API_KEY=
PRIMARY_AI_PROVIDER=auto

# 4. INTEGRATION KEYS
GITHUB_TOKEN=
TELEGRAM_BOT_TOKEN=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

# 5. BACKEND SETTINGS
PROJECT_NAME=Velixo AI Work OS
VERSION=1.0.0
API_V1_STR=/api
```

---

## ⚡ 2. For Vercel (Frontend Deployment)
Copy these key-value pairs into **Vercel Dashboard -> Settings -> Environment Variables**:

| Key | Recommended Value |
| :--- | :--- |
| **`VITE_API_URL`** | `https://your-backend-service.onrender.com` (or your deployed backend URL) |
| `VITE_APP_FIREBASE_API_KEY` | *(Optional Firebase Key)* |

---

## ☁️ 3. For Render / Railway / Backend Hosting
Copy these into your backend deployment service (e.g. Render Environment Variables):

```env
DATABASE_URL=postgresql://neondb_owner:npg_ERJmtbgkO41Q@ep-solitary-shadow-az9g1d2n-pooler.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require
PRIMARY_AI_PROVIDER=auto
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
NVIDIA_API_KEY=your_nvidia_api_key_here
GITHUB_TOKEN=your_github_token_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
PROJECT_NAME=Velixo AI Work OS
VERSION=1.0.0
API_V1_STR=/api
```
