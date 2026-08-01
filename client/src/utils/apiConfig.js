// Dynamic API Base URL Config for Local Development & Vercel Production Deployment
export const API_BASE_URL = (import.meta.env.VITE_API_URL || import.meta.env.VITE_APP_BASE_URL || 'http://localhost:8000').replace(/\/api\/?$/, '');
