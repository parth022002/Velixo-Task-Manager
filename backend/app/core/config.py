import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

DEFAULT_NEON_URL = "postgresql://neondb_owner:npg_ERJmtbgkO41Q@ep-solitary-shadow-az9g1d2n-pooler.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

class Settings(BaseSettings):
    PROJECT_NAME: str = "Velixo AI Work OS"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # API Keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    NVIDIA_API_KEY: str = os.getenv("NVIDIA_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    
    # Active AI Provider: "gemini", "groq", "openrouter", "nvidia", "openai", "ollama", "auto", "mock"
    PRIMARY_AI_PROVIDER: str = os.getenv("PRIMARY_AI_PROVIDER", "auto")
    
    # Neon PostgreSQL Database Connection String
    DATABASE_URL: str = os.getenv("DATABASE_URL", DEFAULT_NEON_URL)
    
    # Integrations
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET", "")
    VITE_APP_FIREBASE_API_KEY: str = os.getenv("VITE_APP_FIREBASE_API_KEY", "")
    
    # Storage & Uploads
    UPLOAD_DIR: str = os.path.join(os.getcwd(), "uploads")
    
    class Config:
        case_sensitive = True

settings = Settings()
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
