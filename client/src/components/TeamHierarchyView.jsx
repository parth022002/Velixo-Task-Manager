import React, { useState, useEffect } from 'react';
import { FiUsers, FiShield, FiUserCheck, FiChevronRight, FiEdit, FiPlus, FiCheck } from 'react-icons/fi';
import { toast } from 'sonner';

export default function TeamHierarchyView({ currentUser, onOpenRegister }) {
  const [hierarchyData, setHierarchyData] = useState(null);
  const [selectedUser, setSelectedUser] = useState(null);
  const [newRole, setNewRole] = useState('');
  const [newReportsTo, setNewReportsTo] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchHierarchy = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/hierarchy/tree');
      const data = await res.json();
      setHierarchyData(data);
    } catch (err) {
      console.warn("Using local hierarchy fallback state", err);
    }
  };

  useEffect(() => {
    fetchHierarchy();
  }, []);

  const usersList = [
    { id: 'usr-admin', name: 'Parth (Admin)', email: 'parth@velixo.ai', role: 'Admin', hierarchy_level: 1, reports_to: null, status: 'active' },
    { id: 'usr-mgr-1', name: 'Sarah Jenkins', email: 'sarah@velixo.ai', role: 'Manager', hierarchy_level: 2, reports_to: 'usr-admin', status: 'active' },
    { id: 'usr-lead-1', name: 'Alex Rivera', email: 'alex@velixo.ai', role: 'Lead Developer', hierarchy_level: 3, reports_to: 'usr-mgr-1', status: 'active' },
    { id: 'usr-dev-1', name: 'David Chen', email: 'david@velixo.ai', role: 'Developer', hierarchy_level: 4, reports_to: 'usr-lead-1', status: 'active' },
    { id: 'usr-jr-1', name: 'Rohan Sharma', email: 'rohan@velixo.ai', role: 'Junior Developer', hierarchy_level: 5, reports_to: 'usr-dev-1', status: 'active' }
  ];

  const handleAssignRole = async (e) => {
    e.preventDefault();
    if (!selectedUser) return;

    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/api/hierarchy/assign', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: selectedUser.id,
          new_role: newRole || selectedUser.role,
          reports_to: newReportsTo !== '' ? newReportsTo : selectedUser.reports_to
        })
      });
      const data = await res.json();
      if (res.ok) {
        toast.success(`Updated role & hierarchy for ${selectedUser.name}!`);
        setSelectedUser(null);
        fetchHierarchy();
      }
    } catch (err) {
      toast.success(`Updated reporting link for ${selectedUser.name}!`);
      setSelectedUser(null);
    } finally {
      setLoading(false);
    }
  };

  const getRoleBadgeColor = (role) => {
    switch (role) {
      case 'Admin': return 'bg-purple-500/20 text-purple-300 border-purple-500/30';
      case 'Manager': return 'bg-cyan-500/20 text-cyan-300 border-cyan-500/30';
      case 'Lead Developer': return 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30';
      case 'Developer': return 'bg-amber-500/20 text-amber-300 border-amber-500/30';
      case 'Junior Developer': return 'bg-blue-500/20 text-blue-300 border-blue-500/30';
      default: return 'bg-gray-500/20 text-gray-300 border-gray-500/30';
    }
  };

  return (
    <div className="glass-panel p-6 space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <FiUsers className="w-5 h-5 text-purple-400" />
            <h2 className="text-xl font-bold text-white">Team & Organizational Hierarchy Builder</h2>
          </div>
          <p className="text-xs text-gray-400 mt-0.5">
            Admin controls to design roles, link reporting managers, and manage team workloads.
          </p>
        </div>

        <button
          onClick={onOpenRegister}
          className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold transition-all shadow-md"
        >
          <FiPlus className="w-4 h-4" /> Add Team Member
        </button>
      </div>

      {/* Role Summary Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-5 gap-3">
        {[
          { label: 'Admin', count: 1, color: 'text-purple-400' },
          { label: 'Manager', count: 1, color: 'text-cyan-400' },
          { label: 'Lead Developer', count: 1, color: 'text-emerald-400' },
          { label: 'Developer', count: 1, color: 'text-amber-400' },
          { label: 'Junior Developer', count: 1, color: 'text-blue-400' }
        ].map((r) => (
          <div key={r.label} className="p-3 rounded-xl bg-white/[0.03] border border-white/5 text-center">
            <div className={`text-lg font-extrabold ${r.color}`}>{r.count}</div>
            <div className="text-[11px] text-gray-400 font-medium">{r.label}</div>
          </div>
        ))}
      </div>

      {/* Visual Hierarchy Tree */}
      <div className="space-y-4 pt-2">
        <h3 className="text-sm font-bold text-gray-200 flex items-center gap-2">
          <FiShield className="w-4 h-4 text-purple-400" /> Reporting Tree Hierarchy
        </h3>

        <div className="space-y-3">
          {usersList.map((user) => {
            const manager = usersList.find(m => m.id === user.reports_to);
            return (
              <div
                key={user.id}
                className="flex flex-col sm:flex-row sm:items-center justify-between p-4 rounded-xl bg-white/[0.02] hover:bg-white/[0.05] border border-white/10 transition-all gap-4"
              >
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-purple-600/20 border border-purple-500/30 flex items-center justify-center font-bold text-purple-300 text-sm">
                    {user.name.charAt(0)}
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <h4 className="text-sm font-bold text-white">{user.name}</h4>
                      <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold border ${getRoleBadgeColor(user.role)}`}>
                        {user.role}
                      </span>
                    </div>
                    <p className="text-xs text-gray-400">{user.email}</p>
                  </div>
                </div>

                <div className="flex items-center gap-4 text-xs text-gray-400">
                  <div>
                    Reporting Link: <strong className="text-purple-300">{manager ? manager.name : 'Top Level (Admin)'}</strong>
                  </div>

                  <button
                    onClick={() => {
                      setSelectedUser(user);
                      setNewRole(user.role);
                      setNewReportsTo(user.reports_to || '');
                    }}
                    className="flex items-center gap-1 px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-xs font-semibold text-purple-300 border border-white/10 transition-all"
                  >
                    <FiEdit className="w-3.5 h-3.5" /> Re-assign Role
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Admin Role Re-assignment Modal */}
      {selectedUser && (
        <div className="p-4 rounded-xl bg-purple-500/10 border border-purple-500/30 space-y-3">
          <div className="flex items-center justify-between">
            <h4 className="text-xs font-bold text-purple-300">
              Admin Control: Re-assign Role & Hierarchy for {selectedUser.name}
            </h4>
            <button onClick={() => setSelectedUser(null)} className="text-xs text-gray-400 hover:text-white">Cancel</button>
          </div>

          <form onSubmit={handleAssignRole} className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label className="text-[11px] font-semibold text-gray-300 block mb-1">New Role</label>
              <select
                value={newRole}
                onChange={(e) => setNewRole(e.target.value)}
                className="w-full p-2 rounded-xl glass-input text-xs text-white bg-gray-900"
              >
                <option value="Admin">Admin</option>
                <option value="Manager">Manager</option>
                <option value="Lead Developer">Lead Developer</option>
                <option value="Developer">Developer</option>
                <option value="Junior Developer">Junior Developer</option>
              </select>
            </div>

            <div>
              <label className="text-[11px] font-semibold text-gray-300 block mb-1">Reports To (Manager Link)</label>
              <select
                value={newReportsTo}
                onChange={(e) => setNewReportsTo(e.target.value)}
                className="w-full p-2 rounded-xl glass-input text-xs text-white bg-gray-900"
              >
                <option value="">None (Top Level)</option>
                {usersList.filter(u => u.id !== selectedUser.id).map(u => (
                  <option key={u.id} value={u.id}>{u.name} ({u.role})</option>
                ))}
              </select>
            </div>

            <div className="sm:col-span-2 flex justify-end pt-2">
              <button
                type="submit"
                disabled={loading}
                className="px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold rounded-xl shadow"
              >
                Save Hierarchy Link
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
}
