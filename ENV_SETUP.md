# 📋 Velixo Master Environment Setup Guide

This file contains all environment variables formatted for quick deployment to **Local `.env`**, **Vercel (Frontend)**, and **Render/Railway (Backend)**.

> 🔒 **Security Note**: Your local `.env` and `backend/.env` files on your computer contain your active API credentials. Never commit plain-text API keys to GitHub.

---

## 🟢 1. Local Development (`.env` & `backend/.env`)
Create a `.env` file in the root directory and in `backend/` containing:

```env
# =====================================================================
# VELIXO ENVIRONMENT CONFIGURATION (.env)
# =====================================================================

# 1. FRONTEND CONFIG
VITE_API_URL=http://localhost:8000
VITE_APP_FIREBASE_API_KEY=your_firebase_api_key_here

# 2. NEON POSTGRESQL DATABASE CONNECTION
DATABASE_URL=postgresql://neondb_owner:npg_ERJmtbgkO41Q@ep-solitary-shadow-az9g1d2n-pooler.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require

# 3. AI PROVIDER API KEYS
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
NVIDIA_API_KEY=your_nvidia_api_key_here
PRIMARY_AI_PROVIDER=auto

# 4. THIRD-PARTY INTEGRATION KEYS
GITHUB_TOKEN=your_github_token_here
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# 5. BACKEND SERVICE SETTINGS
PROJECT_NAME=Velixo AI Work OS
VERSION=1.0.0
API_V1_STR=/api
```

---

## ⚡ 2. For Vercel (Frontend Deployment)
Copy these key-value pairs into **Vercel Dashboard -> Settings -> Environment Variables**:

| Key | Value |
| :--- | :--- |
| **`VITE_API_URL`** | `https://your-backend-service.onrender.com` *(Replace with your live backend Render URL)* |
| `VITE_APP_FIREBASE_API_KEY` | *(Your Firebase Web Push Key)* |

---

## ☁️ 3. For Render / Railway (Backend Hosting)
Copy and paste this raw block directly into **Render -> Web Service -> Environment Variables**:

```env
DATABASE_URL=postgresql://neondb_owner:npg_ERJmtbgkO41Q@ep-solitary-shadow-az9g1d2n-pooler.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require
PRIMARY_AI_PROVIDER=auto
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
NVIDIA_API_KEY=your_nvidia_api_key_here
GITHUB_TOKEN=your_github_token_here
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
PROJECT_NAME=Velixo AI Work OS
VERSION=1.0.0
API_V1_STR=/api
```
