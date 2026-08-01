import React from 'react';
import { FiClock, FiCalendar, FiZap, FiCheckCircle, FiRefreshCw } from 'react-icons/fi';
import { toast } from 'sonner';

export default function AutonomousPlanner({ plannerData, onRefresh }) {
  const schedule = plannerData || {
    daily_theme: "Product Engineering & High-Impact Focus",
    productivity_prediction: 94,
    burnout_risk: "Low",
    recommended_break_time: "14:30 - 14:45",
    blocks: [
      { id: 'b-1', time_slot: "09:00 - 10:30", title: "Deep Work: Architecture & AI Provider Layer", category: "Focus Block", status: "completed", energy_level: "high" },
      { id: 'b-2', time_slot: "10:30 - 11:30", title: "Universal Multimodal Capture & Intent Engine", category: "Execution Block", status: "in_progress", energy_level: "high" },
      { id: 'b-3', time_slot: "11:30 - 12:45", title: "Glassmorphic AI Briefing Center & Visual Dashboard", category: "Focus Block", status: "pending", energy_level: "high" },
      { id: 'b-4', time_slot: "13:45 - 14:30", title: "Predictive Delay Analytics & Gamification Engine", category: "Review Block", status: "pending", energy_level: "medium" },
      { id: 'b-5', time_slot: "15:00 - 16:30", title: "Chief of Staff Multi-Agent Swarm Testing", category: "Execution Block", status: "pending", energy_level: "high" }
    ]
  };

  const getCategoryColor = (cat) => {
    switch (cat) {
      case 'Focus Block': return 'border-purple-500/30 bg-purple-500/10 text-purple-300';
      case 'Execution Block': return 'border-cyan-500/30 bg-cyan-500/10 text-cyan-300';
      case 'Review Block': return 'border-amber-500/30 bg-amber-500/10 text-amber-300';
      default: return 'border-gray-500/30 bg-gray-500/10 text-gray-300';
    }
  };

  return (
    <div className="glass-panel p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <FiCalendar className="w-5 h-5 text-purple-400" />
            <h2 className="text-xl font-bold text-white">Autonomous Daily Planner</h2>
          </div>
          <p className="text-xs text-gray-400 mt-0.5">
            Theme: <strong className="text-purple-300">{schedule.daily_theme}</strong>
          </p>
        </div>

        <div className="flex items-center gap-3">
          <div className="px-3 py-1.5 rounded-xl bg-purple-500/10 border border-purple-500/20 text-xs font-semibold text-purple-300 flex items-center gap-1.5">
            <FiZap className="w-4 h-4 text-purple-400" /> Output: {schedule.productivity_prediction}%
          </div>

          <button
            onClick={() => {
              if (onRefresh) onRefresh();
              toast.success("AI re-optimized calendar schedule based on energy levels!");
            }}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 text-xs font-semibold text-gray-300 transition-all border border-white/10"
          >
            <FiRefreshCw className="w-3.5 h-3.5 text-purple-400" /> Re-Optimize
          </button>
        </div>
      </div>

      {/* Timeline Schedule */}
      <div className="space-y-4 relative before:absolute before:inset-0 before:left-6 before:w-0.5 before:bg-white/10">
        {schedule.blocks.map((block) => (
          <div key={block.id || block.time_slot} className="relative pl-12 flex items-start justify-between group">
            {/* Timeline Circle */}
            <div className={`absolute left-4 top-1.5 w-4 h-4 rounded-full border-2 transform -translate-x-1/2 flex items-center justify-center transition-all ${
              block.status === 'completed'
                ? 'bg-purple-600 border-purple-400 text-white'
                : block.status === 'in_progress'
                ? 'bg-cyan-500 border-cyan-300 animate-pulse'
                : 'bg-gray-800 border-gray-600'
            }`}>
              {block.status === 'completed' && <FiCheckCircle className="w-3 h-3" />}
            </div>

            <div className="w-full glass-panel p-4 flex flex-col md:flex-row md:items-center justify-between gap-3 border border-white/5 hover:border-purple-500/30 transition-all">
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold text-gray-300 flex items-center gap-1">
                    <FiClock className="w-3.5 h-3.5 text-purple-400" /> {block.time_slot}
                  </span>
                  <span className={`px-2 py-0.5 rounded-md text-[10px] font-bold border ${getCategoryColor(block.category)}`}>
                    {block.category}
                  </span>
                </div>
                <h3 className="text-sm font-semibold text-white group-hover:text-purple-300 transition-colors">
                  {block.title}
                </h3>
              </div>

              <div className="flex items-center gap-3">
                <span className="text-xs text-gray-400 font-medium capitalize flex items-center gap-1">
                  <FiZap className="w-3.5 h-3.5 text-amber-400" /> Energy: {block.energy_level}
                </span>

                <span className={`px-2.5 py-1 rounded-lg text-xs font-bold capitalize ${
                  block.status === 'completed'
                    ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                    : block.status === 'in_progress'
                    ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30'
                    : 'bg-gray-800 text-gray-400 border border-gray-700'
                }`}>
                  {block.status.replace('_', ' ')}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
