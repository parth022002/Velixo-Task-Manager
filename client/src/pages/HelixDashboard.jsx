import React, { useState, useEffect } from 'react';
import { Navigate, useNavigate } from 'react-router-dom';
import { 
  FiCpu, 
  FiCalendar, 
  FiShare2, 
  FiPlus, 
  FiSettings, 
  FiActivity,
  FiMessageSquare,
  FiUsers,
  FiUser,
  FiLogOut
} from 'react-icons/fi';
import { Toaster, toast } from 'sonner';

import IntentInputBar from '../components/IntentInputBar';
import ExecutiveBrief from '../components/ExecutiveBrief';
import AutonomousPlanner from '../components/AutonomousPlanner';
import UniversalCaptureModal from '../components/UniversalCaptureModal';
import KnowledgeGraphView from '../components/KnowledgeGraphView';
import ChiefOfStaffChat from '../components/ChiefOfStaffChat';
import AnalyticsGamification from '../components/AnalyticsGamification';
import SettingsModal from '../components/SettingsModal';
import LoginModal from '../components/LoginModal';
import TeamHierarchyView from '../components/TeamHierarchyView';

import PredictiveDashboard from '../components/PredictiveDashboard';
import EveningReviewModal from '../components/EveningReviewModal';
import { FiTrendingUp, FiMoon } from 'react-icons/fi';

export default function HelixDashboard() {
  const [data, setData] = useState(null);
  const [activeTab, setActiveTab] = useState('brief'); // brief, planner, graph, hierarchy, predictive, analytics
  const [isCaptureOpen, setIsCaptureOpen] = useState(false);
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [isAuthOpen, setIsAuthOpen] = useState(false);
  const [isEveningReviewOpen, setIsEveningReviewOpen] = useState(false);
  const [currentUser, setCurrentUser] = useState(() => {
    const saved = localStorage.getItem('velixo_user');
    return saved ? JSON.parse(saved) : null;
  });

  const navigate = useNavigate();

  // Mandatory Authentication Check: If no user session, redirect to login page
  if (!currentUser) {
    return <Navigate to="/login" replace />;
  }

  const fetchDashboardData = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/brief/dashboard');
      const json = await res.json();
      setData(json);
    } catch (err) {
      console.warn("Backend API not reachable yet, using Velixo Local Engine state", err);
    }
  };

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const handleTaskStatusChange = async (taskId, newStatus) => {
    try {
      await fetch(`http://localhost:8000/api/planner/task/${taskId}/status`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus })
      });
      toast.success(`Task status updated to ${newStatus}!`);
      fetchDashboardData();
    } catch (err) {
      toast.success(`Task status updated!`);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('velixo_user');
    setCurrentUser(null);
    toast.info("Logged out of Velixo session.");
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-[#07090e] text-gray-100 flex flex-col font-sans">
      <Toaster richColors position="top-right" />

      {/* Top Navbar with Velixo Logo & User Auth Profile */}
      <header className="sticky top-0 z-40 bg-[#0f1420]/80 backdrop-blur-xl border-b border-white/10 px-4 md:px-8 py-3 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <img 
            src="/logo.png" 
            alt="Velixo Logo" 
            className="w-10 h-10 object-contain drop-shadow-[0_0_15px_rgba(139,92,246,0.6)] hover:scale-105 transition-transform" 
          />
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl font-extrabold text-white tracking-wider font-heading">
                VELIXO
              </h1>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-gradient-to-r from-purple-500/20 to-cyan-500/20 text-purple-300 border border-purple-500/30">
                AI WORK OS
              </span>
            </div>
            <p className="text-[11px] text-gray-400 font-medium">Your AI Chief of Staff for Work and Life</p>
          </div>
        </div>

        {/* Action Controls & User Session Info */}
        <div className="flex items-center gap-2 md:gap-3">
          <div className="flex items-center gap-2">
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-purple-500/10 border border-purple-500/30 text-xs font-semibold text-purple-300">
              <div className="w-5 h-5 rounded-full bg-purple-600 flex items-center justify-center text-[10px] text-white font-bold">
                {currentUser.name ? currentUser.name.charAt(0) : 'U'}
              </div>
              <span>{currentUser.name}</span>
              <span className="px-1.5 py-0.5 text-[9px] font-bold rounded bg-purple-600 text-white capitalize">
                {currentUser.role || 'Developer'}
              </span>
            </div>

            <button
              onClick={handleLogout}
              title="Logout Session"
              className="p-2 rounded-xl bg-white/5 hover:bg-red-500/20 text-gray-400 hover:text-red-300 border border-white/10 transition-all"
            >
              <FiLogOut className="w-4 h-4" />
            </button>
          </div>

          <button
            onClick={() => setIsEveningReviewOpen(true)}
            className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-purple-600/20 hover:bg-purple-600/30 text-purple-300 border border-purple-500/30 text-xs font-bold transition-all"
          >
            <FiMoon className="w-4 h-4 text-purple-400" /> Evening Review
          </button>

          <button
            onClick={() => setIsCaptureOpen(true)}
            className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-500 hover:to-cyan-500 text-white text-xs font-bold shadow-lg shadow-purple-500/20 transition-all active:scale-95"
          >
            <FiPlus className="w-4 h-4" /> Universal Capture
          </button>

          <button
            onClick={() => setIsChatOpen(true)}
            className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 text-purple-300 border border-purple-500/30 text-xs font-semibold transition-all relative"
          >
            <FiMessageSquare className="w-4 h-4 text-purple-400" />
            <span className="hidden sm:inline">Chief of Staff</span>
            <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping absolute -top-0.5 -right-0.5" />
          </button>

          <button
            onClick={() => setIsSettingsOpen(true)}
            title="AI Provider Settings"
            className="p-2 rounded-xl bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10 transition-all"
          >
            <FiSettings className="w-4 h-4" />
          </button>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto p-4 md:p-8 space-y-6">
        {/* Intent Management Bar */}
        <IntentInputBar
          onIntentProcessed={fetchDashboardData}
          onOpenCapture={() => setIsCaptureOpen(true)}
        />

        {/* Dashboard View Navigation Tabs */}
        <div className="flex items-center gap-2 p-1 rounded-2xl glass-panel max-w-3xl mx-auto border border-white/10 overflow-x-auto">
          {[
            { id: 'brief', label: 'Executive Brief', icon: FiCpu },
            { id: 'planner', label: 'Daily Planner', icon: FiCalendar },
            { id: 'graph', label: 'Knowledge Graph', icon: FiShare2 },
            { id: 'hierarchy', label: 'Team & Hierarchy', icon: FiUsers },
            { id: 'predictive', label: 'Predictive & Automation', icon: FiTrendingUp },
            { id: 'analytics', label: 'Analytics & XP', icon: FiActivity }
          ].map((tab) => {
            const Icon = tab.icon;
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex-1 flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                  activeTab === tab.id
                    ? 'bg-gradient-to-r from-purple-600 to-cyan-600 text-white shadow-lg shadow-purple-600/25'
                    : 'text-gray-400 hover:text-white hover:bg-white/5'
                }`}
              >
                <Icon className="w-4 h-4" /> {tab.label}
              </button>
            );
          })}
        </div>

        {/* Tab Content Views */}
        {activeTab === 'brief' && (
          <ExecutiveBrief
            brief={data?.brief}
            tasks={data?.tasks}
            projects={data?.projects}
            onTaskStatusChange={handleTaskStatusChange}
          />
        )}

        {activeTab === 'planner' && (
          <AutonomousPlanner
            plannerData={data?.schedules ? { blocks: data.schedules } : null}
            onRefresh={fetchDashboardData}
          />
        )}

        {activeTab === 'graph' && (
          <KnowledgeGraphView
            graphData={data ? { nodes: data.knowledge_nodes, edges: data.knowledge_edges } : null}
          />
        )}

        {activeTab === 'hierarchy' && (
          <TeamHierarchyView
            currentUser={currentUser}
            onOpenRegister={() => setIsAuthOpen(true)}
          />
        )}

        {activeTab === 'predictive' && (
          <PredictiveDashboard />
        )}

        {activeTab === 'analytics' && (
          <AnalyticsGamification />
        )}
      </main>

      {/* Slideout Drawers and Modals */}
      <UniversalCaptureModal
        isOpen={isCaptureOpen}
        onClose={() => setIsCaptureOpen(false)}
        onCaptureSuccess={fetchDashboardData}
      />

      <ChiefOfStaffChat
        isOpen={isChatOpen}
        onClose={() => setIsChatOpen(false)}
      />

      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={() => setIsSettingsOpen(false)}
      />

      <LoginModal
        isOpen={isAuthOpen}
        onClose={() => setIsAuthOpen(false)}
        onAuthSuccess={(user) => setCurrentUser(user)}
      />

      <EveningReviewModal
        isOpen={isEveningReviewOpen}
        onClose={() => setIsEveningReviewOpen(false)}
      />
    </div>
  );
}
