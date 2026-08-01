import React, { useState } from 'react';
import { FiAward, FiMoon, FiCheckCircle, FiAlertCircle, FiZap, FiX, FiTrendingUp } from 'react-icons/fi';

export default function EveningReviewModal({ isOpen, onClose }) {
  const [completedCount, setCompletedCount] = useState(7);
  const [plannedCount, setPlannedCount] = useState(8);
  const [distraction, setDistraction] = useState('Ad-hoc messaging notifications');
  const [focusMinutes, setFocusMinutes] = useState(240);
  const [reviewResult, setReviewResult] = useState(null);
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleGenerateReview = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/api/coach/evening-review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          completed_tasks_count: parseInt(completedCount),
          planned_tasks_count: parseInt(plannedCount),
          main_distraction: distraction,
          focus_minutes: parseInt(focusMinutes)
        })
      });
      if (res.ok) {
        const data = await res.json();
        setReviewResult(data);
      }
    } catch (err) {
      console.error('Evening Review API error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-md p-4">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl max-w-xl w-full p-6 text-white shadow-2xl space-y-6 relative animate-in fade-in zoom-in duration-200">
        
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-1.5 text-slate-400 hover:text-white bg-slate-800/50 hover:bg-slate-800 rounded-lg transition"
        >
          <FiX className="w-5 h-5" />
        </button>

        {/* Header */}
        <div className="flex items-center space-x-3">
          <div className="p-3 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl shadow-lg">
            <FiMoon className="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 className="text-xl font-bold tracking-tight">Phase 5: AI Coach Evening Review</h2>
            <p className="text-xs text-slate-400">End-of-day execution reflection & tomorrow recommendation</p>
          </div>
        </div>

        {/* Review Form */}
        {!reviewResult ? (
          <div className="space-y-4">
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="text-xs text-slate-400 block mb-1">Completed Tasks</label>
                <input
                  type="number"
                  value={completedCount}
                  onChange={(e) => setCompletedCount(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-purple-500"
                />
              </div>
              <div>
                <label className="text-xs text-slate-400 block mb-1">Planned Tasks</label>
                <input
                  type="number"
                  value={plannedCount}
                  onChange={(e) => setPlannedCount(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-purple-500"
                />
              </div>
            </div>

            <div>
              <label className="text-xs text-slate-400 block mb-1">Focus Time (Minutes)</label>
              <input
                type="number"
                value={focusMinutes}
                onChange={(e) => setFocusMinutes(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-purple-500"
              />
            </div>

            <div>
              <label className="text-xs text-slate-400 block mb-1">Main Distraction Today</label>
              <input
                type="text"
                value={distraction}
                onChange={(e) => setDistraction(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-purple-500"
              />
            </div>

            <button
              onClick={handleGenerateReview}
              disabled={loading}
              className="w-full bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:from-indigo-500 hover:to-pink-500 text-white font-semibold py-2.5 px-4 rounded-xl text-sm transition shadow-lg flex items-center justify-center gap-2"
            >
              <FiZap className="w-4 h-4" /> {loading ? 'Generating Coach Insight...' : 'Generate Evening Reflection'}
            </button>
          </div>
        ) : (
          /* Reflection Result Display */
          <div className="space-y-4">
            <div className="p-4 bg-gradient-to-r from-purple-900/30 to-indigo-900/30 border border-purple-500/30 rounded-xl space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold uppercase tracking-wider text-purple-400">Execution Score</span>
                <span className="px-2.5 py-0.5 bg-emerald-500/20 text-emerald-300 font-extrabold rounded text-sm">
                  {reviewResult.daily_completion_percentage}% ({reviewResult.performance_tier})
                </span>
              </div>

              <div className="space-y-2 text-xs">
                <div className="flex gap-2 text-slate-200">
                  <FiCheckCircle className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                  <div>
                    <span className="font-semibold text-white">Daily Highlight: </span>
                    {reviewResult.key_win}
                  </div>
                </div>

                <div className="flex gap-2 text-slate-200">
                  <FiAlertCircle className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                  <div>
                    <span className="font-semibold text-white">Distraction Pattern: </span>
                    {reviewResult.distraction_insight}
                  </div>
                </div>

                <div className="flex gap-2 text-slate-200">
                  <FiTrendingUp className="w-4 h-4 text-indigo-400 shrink-0 mt-0.5" />
                  <div>
                    <span className="font-semibold text-white">Tomorrow's Strategy: </span>
                    {reviewResult.recommendation_for_tomorrow}
                  </div>
                </div>
              </div>
            </div>

            <button
              onClick={() => setReviewResult(null)}
              className="w-full bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium py-2 rounded-lg text-xs transition"
            >
              ← Conduct Another Evening Reflection
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
