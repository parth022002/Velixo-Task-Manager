import React from 'react';
import { FiAward, FiShield, FiZap, FiStar } from 'react-icons/fi';

export default function AnalyticsGamification() {
  return (
    <div className="glass-panel p-6 space-y-6">
      <div className="flex items-center justify-between border-b border-white/10 pb-4">
        <div className="flex items-center gap-2">
          <FiAward className="w-5 h-5 text-amber-400" />
          <h2 className="text-xl font-bold text-white">Work-Life Gamification & Focus Metrics</h2>
        </div>
        <span className="px-3 py-1 rounded-full text-xs font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/30 flex items-center gap-1">
          <FiStar className="w-3.5 h-3.5 fill-amber-400 text-amber-400" /> Level 14 Chief Strategist
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* XP & Level Progress */}
        <div className="p-4 rounded-xl bg-purple-500/10 border border-purple-500/20 space-y-3">
          <div className="flex items-center justify-between text-xs font-bold">
            <span className="text-purple-300 flex items-center gap-1">
              <FiAward className="w-4 h-4" /> Weekly Productivity XP
            </span>
            <span className="text-white">4,850 / 5,000 XP</span>
          </div>

          <div className="w-full bg-gray-950 rounded-full h-3 overflow-hidden p-0.5 border border-purple-500/30">
            <div className="bg-gradient-to-r from-purple-500 to-cyan-400 h-full rounded-full w-[94%]" />
          </div>

          <p className="text-[11px] text-gray-400">
            150 XP remaining to unlock <strong>Level 15 Executive Orchestration</strong>.
          </p>
        </div>

        {/* Focus Score Analytics */}
        <div className="p-4 rounded-xl bg-cyan-500/10 border border-cyan-500/20 space-y-2">
          <div className="flex items-center justify-between text-xs font-bold text-cyan-300">
            <span className="flex items-center gap-1"><FiZap className="w-4 h-4" /> Focus Deep Work Ratio</span>
            <span className="text-white">91%</span>
          </div>

          <div className="flex items-end justify-between gap-1 h-12 pt-2">
            {[65, 80, 72, 95, 88, 91, 94].map((val, idx) => (
              <div key={idx} className="flex-1 flex flex-col items-center gap-1">
                <div 
                  className="w-full bg-cyan-400/60 rounded-t transition-all hover:bg-cyan-300" 
                  style={{ height: `${val}%` }} 
                />
                <span className="text-[9px] text-gray-400">{['M','T','W','T','F','S','S'][idx]}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Global Rank & Achievements */}
        <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20 space-y-2">
          <div className="flex items-center justify-between text-xs font-bold text-emerald-300">
            <span className="flex items-center gap-1"><FiShield className="w-4 h-4" /> Productivity Rank</span>
            <span className="text-emerald-400">Top 2%</span>
          </div>

          <div className="flex items-center gap-2 pt-2">
            <span className="px-2 py-1 rounded bg-emerald-500/20 text-[10px] font-bold text-emerald-300">
              🔥 7-Day Deep Work Streak
            </span>
            <span className="px-2 py-1 rounded bg-purple-500/20 text-[10px] font-bold text-purple-300">
              🎯 91% Intent Match
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
