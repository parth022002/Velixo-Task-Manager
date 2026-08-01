import React, { useState } from 'react';
import { FiShare2, FiDatabase, FiLayers, FiUser, FiFileText, FiCpu, FiFilter } from 'react-icons/fi';

export default function KnowledgeGraphView({ graphData }) {
  const [filterDomain, setFilterDomain] = useState('all');

  const nodes = graphData?.nodes || [
    { id: 'node-1', label: 'Project Helix AI Work OS', type: 'project', domain: 'professional', details: 'Core Chief of Staff Engine' },
    { id: 'node-2', label: 'Zentrix Startup & Paper', type: 'project', domain: 'professional', details: 'Deep Learning Platform' },
    { id: 'node-3', label: 'AI Chief of Staff', type: 'agent', domain: 'professional', details: 'Multi-Agent Orchestrator' },
    { id: 'node-4', label: 'Universal Capture Engine', type: 'concept', domain: 'professional', details: 'Multimodal Parsing' },
    { id: 'node-5', label: 'Personal Fitness & Wellness', type: 'project', domain: 'personal', details: 'Health & Habits' }
  ];

  const edges = graphData?.edges || [
    { source: 'node-1', target: 'node-3', relation: 'orchestrated_by' },
    { source: 'node-1', target: 'node-4', relation: 'contains' },
    { source: 'node-2', target: 'node-1', relation: 'built_on' },
    { source: 'node-3', target: 'node-5', relation: 'monitors' }
  ];

  const filteredNodes = filterDomain === 'all' 
    ? nodes 
    : nodes.filter(n => n.domain === filterDomain);

  const getNodeColor = (type) => {
    switch (type) {
      case 'project': return 'bg-purple-600/20 border-purple-500 text-purple-300';
      case 'agent': return 'bg-cyan-600/20 border-cyan-500 text-cyan-300';
      case 'concept': return 'bg-amber-600/20 border-amber-500 text-amber-300';
      default: return 'bg-emerald-600/20 border-emerald-500 text-emerald-300';
    }
  };

  return (
    <div className="glass-panel p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <FiShare2 className="w-5 h-5 text-purple-400" />
            <h2 className="text-xl font-bold text-white">Work-Life Knowledge Graph</h2>
          </div>
          <p className="text-xs text-gray-400 mt-0.5">
            Interconnected relationships across projects, tasks, documents, people, and habits.
          </p>
        </div>

        {/* Domain Filter Buttons */}
        <div className="flex items-center gap-1.5 p-1 rounded-xl bg-white/5 border border-white/10">
          {['all', 'professional', 'personal'].map((domain) => (
            <button
              key={domain}
              onClick={() => setFilterDomain(domain)}
              className={`px-3 py-1 rounded-lg text-xs font-semibold capitalize transition-all ${
                filterDomain === domain
                  ? 'bg-purple-600 text-white shadow-md'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              {domain}
            </button>
          ))}
        </div>
      </div>

      {/* SVG Canvas Representation */}
      <div className="relative min-h-[300px] rounded-xl bg-gray-950/60 border border-white/5 p-6 overflow-hidden flex flex-col justify-between">
        <div className="absolute inset-0 opacity-10 bg-[radial-gradient(#8b5cf6_1px,transparent_1px)] [background-size:16px_16px]" />

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 relative z-10">
          {filteredNodes.map((node) => (
            <div
              key={node.id}
              className={`p-4 rounded-xl border backdrop-blur-md transition-all hover:scale-105 ${getNodeColor(node.type)}`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] uppercase tracking-wider font-extrabold px-2 py-0.5 rounded bg-black/40">
                  {node.type}
                </span>
                <span className="text-[10px] text-gray-400 font-medium capitalize">
                  {node.domain}
                </span>
              </div>
              <h3 className="text-sm font-bold text-white mb-1">{node.label}</h3>
              <p className="text-xs text-gray-300">{node.details}</p>
            </div>
          ))}
        </div>

        {/* Legend */}
        <div className="flex flex-wrap items-center gap-4 pt-6 border-t border-white/10 text-xs text-gray-400 relative z-10">
          <span className="flex items-center gap-1.5">
            <span className="w-3 h-3 rounded-full bg-purple-500" /> Projects
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-3 h-3 rounded-full bg-cyan-500" /> AI Agents
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-3 h-3 rounded-full bg-amber-500" /> Concepts & Tools
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-3 h-3 rounded-full bg-emerald-500" /> Personal Wellness
          </span>
        </div>
      </div>
    </div>
  );
}
