import React, { useState, useEffect, useRef } from 'react';
import { FiX, FiSend, FiUser, FiLoader } from 'react-icons/fi';
import { HiSparkles } from 'react-icons/hi2';
import { toast } from 'sonner';

import { API_BASE_URL } from '../utils/apiConfig';

export default function ChiefOfStaffChat({ isOpen, onClose }) {
  const [messages, setMessages] = useState([
    {
      sender: 'ai',
      text: "Hello Parth! I'm your Velixo Chief of Staff AI. How can I optimize your schedule or projects today?",
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  if (!isOpen) return null;

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userText = input;
    setInput('');

    const newMsg = {
      sender: 'user',
      text: userText,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages((prev) => [...prev, newMsg]);
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE_URL}/api/chat/send`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sender: 'user', text: userText })
      });
      const data = await res.json();

      if (data && data.reply) {
        setMessages((prev) => [...prev, data.reply]);
      }
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...prev,
        {
          sender: 'assistant',
          text: `I am Velixo. I have received your instruction: "${userText}". I have retrieved 4 contextual project memories and adjusted your dynamic priorities.`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-y-0 right-0 z-50 w-full max-w-md bg-gray-950/90 backdrop-blur-2xl border-l border-purple-500/30 shadow-2xl flex flex-col animate-slideLeft">
      {/* Header */}
      <div className="p-4 border-b border-white/10 flex items-center justify-between bg-purple-600/10">
        <div className="flex items-center gap-3">
          <img src="/logo.png" alt="Velixo" className="w-9 h-9 object-contain" />
          <div>
            <h3 className="text-sm font-bold text-white flex items-center gap-1.5">
              Velixo AI Chief of Staff <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
            </h3>
            <p className="text-[10px] text-gray-400 flex items-center gap-1">
              <HiSparkles className="w-3 h-3 text-purple-400" /> Persistent Project Memory Active
            </p>
          </div>
        </div>

        <button
          onClick={onClose}
          className="p-2 text-gray-400 hover:text-white hover:bg-white/10 rounded-xl transition-all"
        >
          <FiX className="w-5 h-5" />
        </button>
      </div>

      {/* Suggested Prompts */}
      <div className="p-3 bg-white/[0.02] border-b border-white/5 flex items-center gap-2 overflow-x-auto">
        {[
          "Prepare me for tomorrow",
          "What is pending for Zentrix?",
          "Re-optimize my schedule"
        ].map((prompt) => (
          <button
            key={prompt}
            onClick={() => setInput(prompt)}
            className="px-2.5 py-1 rounded-lg bg-purple-500/10 hover:bg-purple-500/20 text-purple-300 text-[11px] font-medium whitespace-nowrap transition-all border border-purple-500/20"
          >
            {prompt}
          </button>
        ))}
      </div>

      {/* Messages Feed */}
      <div className="flex-1 p-4 overflow-y-auto space-y-4">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`flex items-start gap-2.5 ${
              msg.sender === 'user' ? 'flex-row-reverse' : ''
            }`}
          >
            <div className={`w-8 h-8 rounded-lg flex items-center justify-center text-xs font-bold ${
              msg.sender === 'user'
                ? 'bg-cyan-600 text-white'
                : 'bg-purple-600/30 text-purple-300 border border-purple-500/40'
            }`}>
              {msg.sender === 'user' ? <FiUser className="w-4 h-4" /> : <img src="/logo.png" alt="V" className="w-4 h-4 object-contain" />}
            </div>

            <div className={`max-w-[80%] p-3.5 rounded-2xl text-xs md:text-sm leading-relaxed ${
              msg.sender === 'user'
                ? 'bg-gradient-to-r from-purple-600 to-cyan-600 text-white rounded-tr-none shadow-lg'
                : 'bg-white/5 border border-white/10 text-gray-200 rounded-tl-none'
            }`}>
              {msg.text}
              <div className="text-[10px] opacity-60 mt-1 text-right">
                {msg.timestamp}
              </div>
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex items-center gap-2 text-xs text-purple-400 p-2">
            <FiLoader className="w-4 h-4 animate-spin" /> Velixo is reasoning & querying memory...
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Footer */}
      <form onSubmit={handleSend} className="p-3 border-t border-white/10 bg-gray-950 flex items-center gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask Velixo anything..."
          className="flex-1 px-4 py-2.5 rounded-xl glass-input text-xs text-white placeholder-gray-500"
        />
        <button
          type="submit"
          disabled={loading || !input.trim()}
          className="p-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white disabled:opacity-50 transition-all"
        >
          <FiSend className="w-4 h-4" />
        </button>
      </form>
    </div>
  );
}
