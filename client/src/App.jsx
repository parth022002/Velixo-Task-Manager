import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { Toaster } from "sonner";
import LoginPage from "./pages/LoginPage";
import HelixDashboard from "./pages/HelixDashboard";

function App() {
  return (
    <main className="w-full min-h-screen bg-[#07090e] text-white font-sans">
      <Routes>
        {/* First Page: Mandatory Login / Registration */}
        <Route path="/login" element={<LoginPage />} />
        
        {/* Protected Dashboard Route */}
        <Route path="/dashboard" element={<HelixDashboard />} />
        
        {/* Default route redirects to dashboard (which redirects to /login if unauthenticated) */}
        <Route path="/" element={<HelixDashboard />} />
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
      <Toaster richColors position="top-right" />
    </main>
  );
}

export default App;
