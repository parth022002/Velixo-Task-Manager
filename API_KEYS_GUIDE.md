# 🔑 Velixo AI Work OS: API Keys & Environment Configuration Guide

Velixo is built with a **Provider-Agnostic AI Architecture**. The entire system is designed to run **100% FREE ($0 / ₹0 Budget)** across all phases using free-tier API keys, open-source libraries, and local models.

---

## 🟢 1. Primary Free-Tier AI Providers (Phase 0 & 1)

### A. Google Gemini API Key (Primary Reasoning Model)
* **Cost**: **FREE** (No credit card required. ~1,500 requests/day, 1M tokens/min).
* **How to Get**:
  1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
  2. Click **Get API key** ➔ **Create API key in new project**.
  3. Copy your key (`AIzaSy...`).
* **Environment Variable**: `GEMINI_API_KEY`
> [!WARNING]
> **Billing Trap**: Do NOT enable billing on this Google Cloud project — doing so removes its free tier allowance entirely. Keep a dedicated unpaid project for Velixo.

### B. Groq API Key (Ultra-Fast Llama 3.3 Inference Backup)
* **Cost**: **FREE** (No credit card required. ~30 requests/min, Llama 3.3 70B & Qwen models).
* **How to Get**:
  1. Go to [Groq Console Keys](https://console.groq.com/keys).
  2. Click **Create API Key** and give it a name (e.g. `velixo-dev`).
  3. Copy your key (`gsk_...`).
* **Environment Variable**: `GROQ_API_KEY`

---

## 🟡 2. Extended Free-Model Fallbacks (Phase 1 & 3)

### C. OpenRouter API Key (Rotating Free Catalog)
* **Cost**: **FREE** (20 requests/min; 50 requests/day for `:free` tagged models).
* **How to Get**:
  1. Register at [OpenRouter](https://openrouter.ai).
  2. Open Account Settings ➔ **Keys** ➔ **Create Key** (Leave spending limit at `$0`).
  3. Copy your key (`sk-or-v1-...`).
* **Environment Variable**: `OPENROUTER_API_KEY`

### D. NVIDIA NIM API Key (Hosted Open Models)
* **Cost**: **FREE** (40 requests/min for development and research evaluation).
* **How to Get**:
  1. Sign in at [build.nvidia.com](https://build.nvidia.com).
  2. Select any hosted open model (e.g. `nvidia/nemotron-4-340b-instruct`).
  3. Click **Get API Key** and copy the token.
* **Environment Variable**: `NVIDIA_API_KEY`

---

## 🐘 3. Database & Authentication

| Service | Purpose | Free Allowance | Environment Variable | Signup Link |
| :--- | :--- | :--- | :--- | :--- |
| **Neon PostgreSQL** | Cloud Database + pgvector | 0.5 GB storage, 100 CU hrs/mo | `DATABASE_URL` *(Pre-configured)* | [Neon Tech](https://neon.tech/) |
| **Clerk Auth** | User Authentication | 50,000 monthly active users | `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` | [Clerk Dashboard](https://clerk.com/) |

---

## 🔗 4. Phase 2 & 3 Integration Keys

| Integration | Purpose | How to Setup | Environment Variables |
| :--- | :--- | :--- | :--- |
| **GitHub Token** | PR & Issue Sync | Generate fine-grained token at [GitHub Tokens](https://github.com/settings/tokens) | `GITHUB_TOKEN` |
| **Google Calendar & Gmail API** | 2-Way Sync & Email Task Extraction | Enable Calendar API & Gmail API in [Google Cloud Console](https://console.cloud.google.com) OAuth Consent Screen | `GOOGLE_CLIENT_ID`<br>`GOOGLE_CLIENT_SECRET` |

---

## 🔔 5. Phase 5 Notification Channels

| Service | Purpose | Setup Instructions | Environment Variable |
| :--- | :--- | :--- | :--- |
| **Telegram Bot API** | Direct Chat Push Reminders | Message `@BotFather` on Telegram ➔ Send `/newbot` | `TELEGRAM_BOT_TOKEN` |
| **Firebase FCM** | Browser Web Push | Enable Cloud Messaging at [Firebase Console](https://console.firebase.google.com) | `VITE_APP_FIREBASE_API_KEY` |

> [!NOTE]
> **Why Telegram over WhatsApp?** WhatsApp Business API requires a paid BSP layer ($30+/mo) and per-message fees outside customer service windows. Telegram + Firebase FCM cover 100% free notifications.

---

## 💻 6. Zero-Signup Local Engines (Runs 100% Offline)

These run locally on your system without any external signup or billing:
* 🦙 **Ollama**: Local AI model execution (`llama3`, `qwen3`).
* 🎙️ **Faster-Whisper**: Self-hosted speech-to-text meeting transcription.
* 📄 **EasyOCR / Tesseract**: Self-hosted OCR document reader.
* ⚡ **n8n**: Docker-hosted automation workflow engine.

---

## 🛠️ How to Save Keys in Velixo

### Method 1: Environment File (`.env`)
Place your keys inside `backend/.env`:
```env
GEMINI_API_KEY=AIzaSyYourActualKeyHere
GROQ_API_KEY=gsk_YourGroqKeyHere
OPENROUTER_API_KEY=
NVIDIA_API_KEY=
PRIMARY_AI_PROVIDER=auto
```

### Method 2: Dashboard UI Settings Modal
1. Launch Velixo via `python start_velixo.py` or `run_app.bat`.
2. Open `http://localhost:5173`.
3. Click the **Gear / Settings Icon** in the top navigation bar.
4. Paste your API keys and click **Save Configuration**.