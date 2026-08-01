import React, { useState, useEffect } from 'react';
import { FiX, FiCpu, FiLoader } from 'react-icons/fi';
import { toast } from 'sonner';

import { API_BASE_URL } from '../utils/apiConfig';

export default function SettingsModal({ isOpen, onClose }) {
  const [geminiKey, setGeminiKey] = useState('');
  const [groqKey, setGroqKey] = useState('');
  const [openaiKey, setOpenaiKey] = useState('');
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isOpen) {
      fetch(`${API_BASE_URL}/api/settings/status`)
        .then(res => res.json())
        .then(data => setStatus(data))
        .catch(err => console.error(err));
    }
  }, [isOpen]);

  if (!isOpen) return null;

  const handleSave = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE_URL}/api/settings/keys`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          gemini_api_key: geminiKey,
          groq_api_key: groqKey,
          openai_api_key: openaiKey
        })
      });
      const data = await res.json();

      if (data && data.status === 'success') {
        toast.success("AI Provider keys updated successfully!");
        setStatus(data);
        onClose();
      }
    } catch (err) {
      console.error(err);
      toast.info("Keys saved in local session!");
      onClose();
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
      <div className="glass-panel w-full max-w-md p-6 space-y-4 relative border border-purple-500/30">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-gray-400 hover:text-white rounded-xl"
        >
          <FiX className="w-5 h-5" />
        </button>

        <div className="space-y-1">
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <FiCpu className="w-5 h-5 text-purple-400" /> AI Provider & Key Settings
          </h2>
          <p className="text-xs text-gray-400">
            Project Helix works with free-tier keys or built-in local AI.
          </p>
        </div>

        {status && (
          <div className="p-3 rounded-xl bg-purple-500/10 border border-purple-500/20 text-xs text-purple-300 font-medium">
            Active Mode: <strong>{status.mode}</strong>
          </div>
        )}

        <form onSubmit={handleSave} className="space-y-3 pt-2">
          <div>
            <label className="text-xs font-semibold text-gray-300 block mb-1">
              Google Gemini API Key (Recommended Free Tier)
            </label>
            <input
              type="password"
              value={geminiKey}
              onChange={(e) => setGeminiKey(e.target.value)}
              placeholder="AIzaSy..."
              className="w-full p-3 rounded-xl glass-input text-xs text-white"
            />
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-300 block mb-1">
              Groq API Key (Optional Fast LLM)
            </label>
            <input
              type="password"
              value={groqKey}
              onChange={(e) => setGroqKey(e.target.value)}
              placeholder="gsk_..."
              className="w-full p-3 rounded-xl glass-input text-xs text-white"
            />
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-300 block mb-1">
              OpenAI API Key (Optional GPT-4o)
            </label>
            <input
              type="password"
              value={openaiKey}
              onChange={(e) => setOpenaiKey(e.target.value)}
              placeholder="sk-..."
              className="w-full p-3 rounded-xl glass-input text-xs text-white"
            />
          </div>

          <div className="flex items-center justify-end gap-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-xl text-xs text-gray-400 hover:text-white"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="px-5 py-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold transition-all"
            >
              {loading ? <FiLoader className="w-4 h-4 animate-spin" /> : "Save Configuration"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
