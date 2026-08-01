// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

// Velixo Production Firebase Configuration
const firebaseConfig = {
    apiKey: import.meta.env.VITE_APP_FIREBASE_API_KEY || "AIzaSyBXXX4lPOX8GbCydXErADLkyzMZu1ZVL8c",
    authDomain: "velixo-7f362.firebaseapp.com",
    projectId: "velixo-7f362",
    storageBucket: "velixo-7f362.firebasestorage.app",
    messagingSenderId: "694068248841",
    appId: "1:694068248841:web:33b93ee4c4164b30b753d8",
    measurementId: "G-PZ43XECYFS"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const analytics = typeof window !== "undefined" ? getAnalytics(app) : null;
export default app;