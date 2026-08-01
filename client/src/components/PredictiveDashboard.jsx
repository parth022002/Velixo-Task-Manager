import React, { useState } from 'react';
import { FiShield, FiCpu, FiZap, FiActivity, FiClock, FiAlertTriangle, FiCheckCircle, FiPlay } from 'react-icons/fi';

import { API_BASE_URL } from '../utils/apiConfig';

export default function PredictiveDashboard() {
  const [availableHours, setAvailableHours] = useState(5.0);
  const [energyLevel, setEnergyLevel] = useState('High');
  const [capacityPlan, setCapacityPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [automationLog, setAutomationLog] = useState([
    { id: 1, event: 'UNPAID_INVOICE', status: 'Completed', detail: 'Sent Telegram alert to @Velixo_Task_Manager_Bot & updated brief widget' },
    { id: 2, event: 'OVERDUE_TASK', status: 'Completed', detail: 'Recalculated priority score to CRITICAL (94.5) & rescheduled focus block' }
  ]);

  const handleEvaluateCapacity = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/predictive/capacity-decision`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          available_hours: parseFloat(availableHours),
          energy_level: energyLevel,
          primary_goal: 'Ship Velixo Production Roadmap'
        })
      });
      if (res.ok) {
        const data = await res.json();
        setCapacityPlan(data.optimized_action_plan);
      }
    } catch (err) {
      console.error('Capacity API error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleTriggerAutomation = async (eventType) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/automation/trigger`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          event_type: eventType,
          payload: { timestamp: new Date().toISOString() }
        })
      });
      if (res.ok) {
        const data = await res.json();
        setAutomationLog(prev => [
          { id: Date.now(), event: eventType, status: 'Completed', detail: data.action_chain_steps.join(' -> ') },
          ...prev
        ]);
      }
    } catch (err) {
      console.error('Automation trigger error:', err);
    }
  };

  return (
    <div className="bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-2xl p-6 text-white shadow-2xl space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div className="flex items-center space-x-3">
          <div className="p-2.5 bg-gradient-to-r from-amber-500 to-indigo-600 rounded-xl shadow-lg">
            <FiCpu className="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 className="text-xl font-bold tracking-tight">Phase 4: Predictive Intelligence & Automation</h2>
            <p className="text-sm text-slate-400">Delay Risk Modeling • Burnout Prevention • n8n Action Chains</p>
          </div>
        </div>
        <span className="px-3 py-1 bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-semibold rounded-full flex items-center gap-1.5">
          <FiActivity className="w-3.5 h-3.5 animate-pulse" /> Live ML Engine
        </span>
      </div>

      {/* Risk Metrics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-slate-800/50 border border-slate-700/50 rounded-xl p-4 space-y-2">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold uppercase tracking-wider">
            <span>Project Delay Risk</span>
            <FiAlertTriangle className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="text-2xl font-extrabold text-emerald-400">12.0%</div>
          <p className="text-xs text-slate-400">Velixo Roadmap is 100% on schedule.</p>
        </div>

        <div className="bg-slate-800/50 border border-slate-700/50 rounded-xl p-4 space-y-2">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold uppercase tracking-wider">
            <span>Burnout Risk Index</span>
            <FiShield className="w-4 h-4 text-amber-400" />
          </div>
          <div className="text-2xl font-extrabold text-amber-400">LOW</div>
          <p className="text-xs text-slate-400">Daily workload is well balanced.</p>
        </div>

        <div className="bg-slate-800/50 border border-slate-700/50 rounded-xl p-4 space-y-2">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold uppercase tracking-wider">
            <span>Active Action Chains</span>
            <FiZap className="w-4 h-4 text-indigo-400" />
          </div>
          <div className="text-2xl font-extrabold text-indigo-400">{automationLog.length} Chains</div>
          <p className="text-xs text-slate-400">n8n Automated workflows active.</p>
        </div>
      </div>

      {/* Capacity Decision Engine */}
      <div className="bg-slate-800/30 border border-slate-800 rounded-xl p-5 space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-md font-semibold text-slate-200 flex items-center gap-2">
            <FiClock className="w-4 h-4 text-indigo-400" /> AI Capacity Decision Engine
          </h3>
          <span className="text-xs text-slate-400">"I have X hours today — what should I do?"</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          <div>
            <label className="text-xs text-slate-400 block mb-1">Available Hours Today</label>
            <input
              type="number"
              step="0.5"
              value={availableHours}
              onChange={(e) => setAvailableHours(e.target.value)}
              className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500"
            />
          </div>
          <div>
            <label className="text-xs text-slate-400 block mb-1">Energy Level</label>
            <select
              value={energyLevel}
              onChange={(e) => setEnergyLevel(e.target.value)}
              className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500"
            >
              <option value="High">⚡ High Energy</option>
              <option value="Medium">⚖️ Medium Energy</option>
              <option value="Low">😴 Low Energy</option>
            </select>
          </div>
          <div className="flex items-end">
            <button
              onClick={handleEvaluateCapacity}
              disabled={loading}
              className="w-full bg-gradient-to-r from-indigo-600 to-indigo-700 hover:from-indigo-500 hover:to-indigo-600 text-white font-medium py-2 px-4 rounded-lg text-sm transition-all shadow-md flex items-center justify-center gap-2"
            >
              <FiPlay className="w-4 h-4" /> {loading ? 'Evaluating...' : 'Optimize Schedule'}
            </button>
          </div>
        </div>

        {capacityPlan && (
          <div className="mt-4 space-y-2 border-t border-slate-800 pt-3">
            <h4 className="text-xs font-semibold text-indigo-400 uppercase tracking-wider">Optimized Time Block Recommendations:</h4>
            <div className="space-y-2">
              {capacityPlan.map((block, idx) => (
                <div key={idx} className="bg-slate-900/60 border border-slate-800 rounded-lg p-3 flex items-center justify-between text-xs">
                  <div>
                    <span className="font-semibold text-white">{block.time_slot}</span>
                    <span className="text-slate-400 ml-2">({block.focus_type})</span>
                    <p className="text-slate-300 mt-0.5">{block.recommended_task}</p>
                  </div>
                  <span className="px-2 py-0.5 bg-indigo-500/20 text-indigo-300 font-bold rounded">
                    {block.priority}
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Action Chains Execution Log */}
      <div className="space-y-3 border-t border-slate-800 pt-4">
        <div className="flex items-center justify-between">
          <h3 className="text-sm font-semibold text-slate-300 flex items-center gap-2">
            <FiZap className="w-4 h-4 text-amber-400" /> Live n8n Automated Action Chains
          </h3>
          <div className="flex gap-2">
            <button
              onClick={() => handleTriggerAutomation('UNPAID_INVOICE')}
              className="px-2.5 py-1 bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 border border-amber-500/30 rounded-md text-xs font-medium transition"
            >
              + Trigger Unpaid Invoice Chain
            </button>
            <button
              onClick={() => handleTriggerAutomation('OVERDUE_TASK')}
              className="px-2.5 py-1 bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/30 rounded-md text-xs font-medium transition"
            >
              + Trigger Overdue Task Chain
            </button>
          </div>
        </div>

        <div className="space-y-2">
          {automationLog.map(item => (
            <div key={item.id} className="bg-slate-800/40 border border-slate-700/40 rounded-lg p-3 flex items-center justify-between text-xs">
              <div className="flex items-center gap-2.5">
                <FiCheckCircle className="w-4 h-4 text-emerald-400" />
                <div>
                  <span className="font-bold text-white">{item.event}</span>
                  <p className="text-slate-400 mt-0.5">{item.detail}</p>
                </div>
              </div>
              <span className="px-2 py-0.5 bg-emerald-500/20 text-emerald-300 rounded font-medium">
                {item.status}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
