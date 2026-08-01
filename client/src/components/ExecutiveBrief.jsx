import React from 'react';
import { 
  FiCpu, 
  FiActivity, 
  FiAlertTriangle, 
  FiCheckCircle, 
  FiClock, 
  FiTrendingUp, 
  FiChevronRight,
  FiVolume2
} from 'react-icons/fi';
import { toast } from 'sonner';

export default function ExecutiveBrief({ brief, tasks = [], projects = [], onTaskStatusChange }) {
  const currentBrief = brief || {
    date: 'Wednesday, July 30, 2026',
    brief_summary: "Good morning! Today we are focusing on launching Velixo core AI modules. You have 3 critical tasks and 5 schedule blocks lined up.",
    focus_score: 91,
    health_score: 82,
    burnout_risk: "Low",
    total_tasks: tasks.length || 8,
    critical_tasks: 3
  };

  const topPriorities = tasks.length > 0 ? tasks.slice(0, 3) : [
    { id: 't-1', title: 'Build Velixo AI Provider Layer & Fallback Engine', priority: 'CRITICAL', priority_score: 96.5, domain: 'professional', estimated_minutes: 45, status: 'completed' },
    { id: 't-2', title: 'Finalize Universal Capture Engine & Intent Parser', priority: 'HIGH', priority_score: 88.0, domain: 'professional', estimated_minutes: 60, status: 'in_progress' },
    { id: 't-3', title: 'Review Reinforcement Learning Paper for Zentrix', priority: 'HIGH', priority_score: 82.0, domain: 'professional', estimated_minutes: 90, status: 'pending' }
  ];

  const handleReadAloud = () => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(currentBrief.brief_summary);
      utterance.pitch = 1.0;
      utterance.rate = 1.0;
      window.speechSynthesis.speak(utterance);
      toast.success("Velixo AI Chief of Staff reading morning briefing aloud...");
    } else {
      toast.info(currentBrief.brief_summary);
    }
  };

  return (
    <div className="w-full space-y-6">
      {/* Header Banner */}
      <div className="glass-panel p-6 relative overflow-hidden border border-purple-500/20 shadow-2xl">
        <div className="absolute top-0 right-0 w-96 h-96 bg-purple-600/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-cyan-600/10 rounded-full blur-3xl pointer-events-none" />

        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 relative z-10">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30 flex items-center gap-1.5">
                <img src="/logo.png" alt="Velixo" className="w-4 h-4 object-contain" /> Velixo Briefing Center
              </span>
              <span className="text-xs text-gray-400 font-medium">{currentBrief.date}</span>
            </div>
            <h1 className="text-2xl md:text-3xl font-bold text-white tracking-tight">
              Good Morning! Your <span className="gradient-text">Velixo Chief of Staff</span> Summary
            </h1>
            <p className="text-sm text-gray-300 max-w-3xl leading-relaxed pt-1">
              "{currentBrief.brief_summary}"
            </p>
          </div>

          <button
            onClick={handleReadAloud}
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-semibold text-purple-300 transition-all shadow-md self-start md:self-auto"
          >
            <FiVolume2 className="w-4 h-4 text-purple-400" /> Listen Brief
          </button>
        </div>

        {/* Metrics Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-6 pt-6 border-t border-white/10">
          <div className="flex items-center gap-3">
            <div className="p-3 rounded-xl bg-purple-500/10 border border-purple-500/20 text-purple-400">
              <FiActivity className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xs text-gray-400 font-medium">Focus Score</div>
              <div className="text-xl font-extrabold text-white">{currentBrief.focus_score}%</div>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400">
              <FiActivity className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xs text-gray-400 font-medium">Health Score</div>
              <div className="text-xl font-extrabold text-white">{currentBrief.health_score}%</div>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <div className="p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400">
              <FiTrendingUp className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xs text-gray-400 font-medium">Burnout Risk</div>
              <div className="text-xl font-extrabold text-amber-300">{currentBrief.burnout_risk}</div>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <div className="p-3 rounded-xl bg-cyan-500/10 border border-cyan-500/20 text-cyan-400">
              <FiAlertTriangle className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xs text-gray-400 font-medium">Critical Tasks</div>
              <div className="text-xl font-extrabold text-white">{currentBrief.critical_tasks} <span className="text-xs text-gray-400 font-normal">/ {currentBrief.total_tasks}</span></div>
            </div>
          </div>
        </div>
      </div>

      {/* Top Priorities Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 glass-panel p-6 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <FiActivity className="w-5 h-5 text-purple-400" />
              <h2 className="text-lg font-bold text-white">Top Priority Actions (Velixo Ranked)</h2>
            </div>
            <span className="text-xs text-gray-400">Auto-updated by Velixo Priority Engine</span>
          </div>

          <div className="space-y-3">
            {topPriorities.map((task) => (
              <div
                key={task.id || task.title}
                className="flex items-center justify-between p-4 rounded-xl bg-white/[0.03] hover:bg-white/[0.06] border border-white/5 transition-all group"
              >
                <div className="flex items-center gap-3 flex-1 pr-4">
                  <button
                    onClick={() => onTaskStatusChange && onTaskStatusChange(task.id, task.status === 'completed' ? 'pending' : 'completed')}
                    className={`w-5 h-5 rounded-md border flex items-center justify-center transition-all ${
                      task.status === 'completed'
                        ? 'bg-purple-600 border-purple-500 text-white'
                        : 'border-gray-500 hover:border-purple-400'
                    }`}
                  >
                    {task.status === 'completed' && <FiCheckCircle className="w-4 h-4" />}
                  </button>

                  <div className="space-y-0.5">
                    <h3 className={`text-sm font-semibold ${task.status === 'completed' ? 'line-through text-gray-500' : 'text-gray-200'}`}>
                      {task.title}
                    </h3>
                    <div className="flex items-center gap-2 text-xs text-gray-400">
                      <span className="px-2 py-0.5 rounded bg-white/5 text-purple-300 font-medium capitalize">
                        {task.domain}
                      </span>
                      <span className="flex items-center gap-1 text-gray-400">
                        <FiClock className="w-3 h-3" /> {task.estimated_minutes || 45} mins
                      </span>
                    </div>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <div className="text-right">
                    <div className="text-xs font-bold text-purple-400">Score {task.priority_score || 85}</div>
                    <div className="text-[10px] text-gray-400 font-medium uppercase">{task.priority}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Predictive Project Risk Widget */}
        <div className="glass-panel p-6 space-y-4 flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 mb-3">
              <FiAlertTriangle className="w-5 h-5 text-amber-400" />
              <h2 className="text-lg font-bold text-white">Predictive Risk Analysis</h2>
            </div>
            <p className="text-xs text-gray-400 leading-relaxed mb-4">
              AI predicts project delay risks based on scope changes and resource bottlenecks before they happen.
            </p>

            <div className="p-4 rounded-xl bg-amber-500/10 border border-amber-500/20 space-y-2">
              <div className="flex items-center justify-between text-xs font-bold text-amber-300">
                <span>Zentrix Backend API</span>
                <span>Est. Delay: 2 Days</span>
              </div>
              <p className="text-xs text-gray-300">
                Cause: GPU compute allocation bottleneck and missing dependency specs.
              </p>
              <div className="w-full bg-gray-800 rounded-full h-1.5 mt-2 overflow-hidden">
                <div className="bg-amber-400 h-full rounded-full w-[78%]" />
              </div>
            </div>
          </div>

          <div className="pt-4 border-t border-white/10 flex items-center justify-between text-xs text-gray-400">
            <span>Velixo Risk Monitor: Active</span>
            <span className="text-purple-400 font-semibold flex items-center gap-1 cursor-pointer hover:underline">
              View All <FiChevronRight className="w-3 h-3" />
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
