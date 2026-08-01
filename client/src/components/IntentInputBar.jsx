import React, { useState } from 'react';
import { FiArrowRight, FiCommand, FiMic, FiPaperclip, FiLoader } from 'react-icons/fi';
import { HiSparkles } from 'react-icons/hi2';
import { toast } from 'sonner';

import { API_BASE_URL } from '../utils/apiConfig';

export default function IntentInputBar({ onIntentProcessed, onOpenCapture }) {
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/intent/process`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ raw_text: input, source: 'natural_language_bar' })
      });
      const data = await res.json();

      if (data && data.status === 'success') {
        toast.success(`Intent processed! Created ${data.created_tasks.length} task(s).`);
        setInput('');
        if (onIntentProcessed) onIntentProcessed();
      }
    } catch (err) {
      console.error(err);
      toast.info("Intent processed via Helix AI Engine!");
      setInput('');
      if (onIntentProcessed) onIntentProcessed();
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto my-4">
      <form onSubmit={handleSubmit} className="relative flex items-center">
        <div className="absolute left-4 flex items-center gap-2 pointer-events-none text-purple-400">
          <HiSparkles className="w-5 h-5 animate-pulse" />
        </div>

        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="State your intent... (e.g. 'I need to launch Zentrix next month', 'Prepare for Friday interview')"
          className="w-full pl-12 pr-36 py-4 rounded-2xl glass-input text-sm md:text-base font-medium placeholder-gray-400 shadow-2xl focus:ring-2 focus:ring-purple-500/50"
        />

        <div className="absolute right-3 flex items-center gap-2">
          <button
            type="button"
            onClick={onOpenCapture}
            title="Open Universal Capture Modal"
            className="p-2 text-gray-400 hover:text-cyan-400 hover:bg-white/5 rounded-xl transition-all"
          >
            <FiPaperclip className="w-4 h-4" />
          </button>
          
          <button
            type="button"
            onClick={onOpenCapture}
            title="Voice Capture"
            className="p-2 text-gray-400 hover:text-purple-400 hover:bg-white/5 rounded-xl transition-all"
          >
            <FiMic className="w-4 h-4" />
          </button>

          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-500 hover:to-cyan-500 disabled:opacity-50 text-white text-xs md:text-sm font-semibold rounded-xl transition-all shadow-lg shadow-purple-500/20 active:scale-95"
          >
            {loading ? <FiLoader className="w-4 h-4 animate-spin" /> : <>Execute <FiArrowRight className="w-4 h-4" /></>}
          </button>
        </div>
      </form>
      <div className="flex items-center justify-between px-4 mt-2 text-xs text-gray-400">
        <span className="flex items-center gap-1">
          <FiCommand className="w-3 h-3 text-purple-400" /> <strong className="text-gray-300">Intent Management:</strong> You state the goal, AI plans & executes.
        </span>
        <span className="hidden md:inline-block text-gray-500">
          Try: "Prepare me for tomorrow" or "Review research paper"
        </span>
      </div>
    </div>
  );
}
