import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FiUser, FiLock, FiMail, FiShield, FiArrowRight, FiCheckCircle, FiLoader } from 'react-icons/fi';
import { HiSparkles } from 'react-icons/hi2';
import { toast } from 'sonner';

import { API_BASE_URL } from '../utils/apiConfig';

export default function LoginPage() {
  const [isRegister, setIsRegister] = useState(false);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('parth@velixo.ai');
  const [password, setPassword] = useState('adminpassword123');
  const [role, setRole] = useState('Admin');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleAuth = async (e) => {
    e.preventDefault();
    if (!email || !password) return;

    setLoading(true);
    const endpoint = isRegister ? `${API_BASE_URL}/api/auth/register` : `${API_BASE_URL}/api/auth/login`;

    try {
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: isRegister ? name : undefined,
          email,
          password,
          role: isRegister ? role : undefined
        })
      });
      const data = await res.json();

      if (res.ok && data.status === 'success') {
        toast.success(isRegister ? "Account created successfully!" : `Welcome back, ${data.user.name}!`);
        localStorage.setItem('velixo_user', JSON.stringify(data.user));
        navigate('/dashboard');
      } else {
        toast.error(data.detail || "Authentication failed.");
      }
    } catch (err) {
      console.warn("API offline fallback sign in", err);
      const fallbackUser = {
        id: 'usr-admin',
        name: isRegister ? (name || 'New User') : (email.includes('sarah') ? 'Sarah Jenkins' : 'Parth (Admin)'),
        email: email,
        role: isRegister ? role : (email.includes('sarah') ? 'Manager' : 'Admin'),
        avatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=Admin'
      };
      localStorage.setItem('velixo_user', JSON.stringify(fallbackUser));
      toast.success(`Signed in as ${fallbackUser.name} (${fallbackUser.role})`);
      navigate('/dashboard');
    } finally {
      setLoading(false);
    }
  };

  const setDemoUser = (demoEmail, demoPass, demoRole, demoName) => {
    setEmail(demoEmail);
    setPassword(demoPass);
    setRole(demoRole);
    setName(demoName);
    setIsRegister(false);
    toast.info(`Preloaded ${demoName} (${demoRole}) credentials`);
  };

  return (
    <div className="min-h-screen bg-[#07090e] text-white flex flex-col justify-center items-center p-4 relative overflow-hidden font-sans">
      {/* Ambient background glows */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-purple-600/15 rounded-full blur-3xl pointer-events-none animate-pulse-glow" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-cyan-600/15 rounded-full blur-3xl pointer-events-none animate-pulse-glow" />

      {/* Main Glassmorphic Auth Card */}
      <div className="glass-panel w-full max-w-md p-8 relative border border-purple-500/30 shadow-2xl space-y-6">
        {/* Brand Header */}
        <div className="text-center space-y-2">
          <div className="inline-flex items-center justify-center p-2 rounded-2xl bg-white/5 border border-white/10 mb-1">
            <img 
              src="/logo.png" 
              alt="Velixo Logo" 
              className="w-12 h-12 object-contain drop-shadow-[0_0_15px_rgba(139,92,246,0.8)]" 
            />
          </div>
          <h1 className="text-2xl font-extrabold tracking-wider font-heading text-white">
            VELIXO <span className="gradient-text">AI WORK OS</span>
          </h1>
          <p className="text-xs text-gray-400 font-medium flex items-center justify-center gap-1">
            <HiSparkles className="text-purple-400" /> Your AI Chief of Staff for Work and Life
          </p>
        </div>

        {/* Tab Switcher: Sign In vs Register */}
        <div className="flex rounded-xl bg-white/5 p-1 border border-white/10">
          <button
            type="button"
            onClick={() => setIsRegister(false)}
            className={`flex-1 py-2 text-xs font-bold rounded-lg transition-all ${
              !isRegister ? 'bg-purple-600 text-white shadow-lg shadow-purple-600/30' : 'text-gray-400 hover:text-white'
            }`}
          >
            Sign In
          </button>
          <button
            type="button"
            onClick={() => setIsRegister(true)}
            className={`flex-1 py-2 text-xs font-bold rounded-lg transition-all ${
              isRegister ? 'bg-purple-600 text-white shadow-lg shadow-purple-600/30' : 'text-gray-400 hover:text-white'
            }`}
          >
            Create Account
          </button>
        </div>

        {/* Form */}
        <form onSubmit={handleAuth} className="space-y-4">
          {isRegister && (
            <div>
              <label className="text-xs font-semibold text-gray-300 block mb-1">Full Name</label>
              <div className="relative">
                <FiUser className="absolute left-3.5 top-3.5 text-gray-500 w-4 h-4" />
                <input
                  type="text"
                  required={isRegister}
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="e.g. Sarah Jenkins"
                  className="w-full pl-10 pr-4 py-3 rounded-xl glass-input text-xs text-white"
                />
              </div>
            </div>
          )}

          <div>
            <label className="text-xs font-semibold text-gray-300 block mb-1">Email Address</label>
            <div className="relative">
              <FiMail className="absolute left-3.5 top-3.5 text-gray-500 w-4 h-4" />
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="parth@velixo.ai"
                className="w-full pl-10 pr-4 py-3 rounded-xl glass-input text-xs text-white"
              />
            </div>
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-300 block mb-1">Password</label>
            <div className="relative">
              <FiLock className="absolute left-3.5 top-3.5 text-gray-500 w-4 h-4" />
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full pl-10 pr-4 py-3 rounded-xl glass-input text-xs text-white"
              />
            </div>
          </div>

          {isRegister && (
            <div>
              <label className="text-xs font-semibold text-gray-300 block mb-1">Select Organizational Role</label>
              <div className="relative">
                <FiShield className="absolute left-3.5 top-3.5 text-gray-500 w-4 h-4" />
                <select
                  value={role}
                  onChange={(e) => setRole(e.target.value)}
                  className="w-full pl-10 pr-4 py-3 rounded-xl glass-input text-xs text-white bg-gray-900"
                >
                  <option value="Admin">Admin (Full System & Hierarchy Control)</option>
                  <option value="Manager">Manager (Team & Project Lead)</option>
                  <option value="Lead Developer">Lead Developer (Architecture)</option>
                  <option value="Developer">Developer (Core Tasks)</option>
                  <option value="Junior Developer">Junior Developer (Execution)</option>
                </select>
              </div>
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full flex items-center justify-center gap-2 py-3 rounded-xl bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-500 hover:to-cyan-500 text-white text-xs font-bold transition-all shadow-lg shadow-purple-500/25 active:scale-95 mt-2"
          >
            {loading ? <FiLoader className="w-4 h-4 animate-spin" /> : <>{isRegister ? "Register & Enter Velixo" : "Sign In to Velixo"} <FiArrowRight className="w-4 h-4" /></>}
          </button>
        </form>

        {/* Quick Demo Login Preset Buttons */}
        <div className="pt-4 border-t border-white/10 space-y-2">
          <span className="text-[11px] text-gray-400 font-medium block text-center">Quick Demo Presets (1-Click Login)</span>
          <div className="grid grid-cols-2 gap-2">
            <button
              type="button"
              onClick={() => setDemoUser('parth@velixo.ai', 'adminpassword123', 'Admin', 'Parth (Admin)')}
              className="px-3 py-2 rounded-xl bg-purple-500/10 hover:bg-purple-500/20 text-purple-300 text-[11px] font-semibold border border-purple-500/20 text-left transition-all"
            >
              👑 Parth (Admin)
            </button>

            <button
              type="button"
              onClick={() => setDemoUser('sarah@velixo.ai', 'password123', 'Manager', 'Sarah Jenkins')}
              className="px-3 py-2 rounded-xl bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-300 text-[11px] font-semibold border border-cyan-500/20 text-left transition-all"
            >
              📊 Sarah (Manager)
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
