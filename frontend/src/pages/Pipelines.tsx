import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Play, Plus, Trash2, Settings, Save, GitBranch, Activity } from 'lucide-react';
import { toast } from 'react-hot-toast';
import Layout from '../components/Layout';

const Pipelines = () => {
  const [nodes, setNodes] = useState([
    { id: 1, type: 'Input', name: 'Sales Dataset', color: 'bg-blue-500' },
    { id: 2, type: 'Clean', name: 'Remove Nulls', color: 'bg-yellow-500' },
    { id: 3, type: 'Transform', name: 'Aggregate Revenue', color: 'bg-purple-500' },
    { id: 4, type: 'Output', name: 'PostgreSQL Sync', color: 'bg-green-500' },
  ]);

  const [executing, setExecuting] = useState(false);

  const handleExecute = () => {
    setExecuting(true);
    const toastId = toast.loading('Initializing pipeline execution environment...');
    setTimeout(() => {
      setExecuting(false);
      toast.success('Pipeline execution completed successfully!', { id: toastId });
    }, 3000);
  };

  const handleSave = () => {
    toast.success('Pipeline draft saved.');
  };

  return (
    <Layout>
      <div className="flex flex-col h-[calc(100vh-140px)]">
        
        {/* Top Header / Toolbar */}
        <div className="bg-white border border-gray-200 rounded-2xl px-6 py-4 flex justify-between items-center shadow-sm mb-6 dark:bg-gray-800 dark:border-gray-700">
          <div>
            <h1 className="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
              <GitBranch className="text-blue-600 w-5 h-5" /> Revenue Aggregation Pipeline
            </h1>
            <p className="text-gray-500 text-sm mt-1">Status: <span className="text-green-600 font-semibold">Active</span></p>
          </div>
          
          <div className="flex gap-4">
            <button onClick={handleSave} className="flex items-center gap-2 px-4 py-2 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-600 font-medium transition shadow-sm">
              <Save className="w-4 h-4" /> Save Draft
            </button>
            <button 
              onClick={handleExecute}
              disabled={executing}
              className={`flex items-center gap-2 px-6 py-2 rounded-lg font-bold text-white transition shadow-md ${
                executing ? 'bg-blue-400 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700 shadow-blue-500/30'
              }`}
            >
              {executing ? (
                <><Activity className="w-4 h-4 animate-spin" /> Executing...</>
              ) : (
                <><Play className="w-4 h-4" /> Run Pipeline</>
              )}
            </button>
          </div>
        </div>

        <div className="flex-1 flex gap-6 overflow-hidden">
          {/* Left Panel: Node Palette */}
          <div className="w-64 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-2xl p-5 overflow-y-auto shadow-sm">
            <h3 className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-4">Available Nodes</h3>
            <div className="space-y-3">
              {['Input Source', 'Filter Data', 'Join Datasets', 'Machine Learning', 'Export to BI'].map((node, i) => (
                <div key={i} className="p-3 border border-gray-100 dark:border-gray-700 rounded-xl cursor-grab bg-gray-50 dark:bg-gray-900 flex items-center justify-between group hover:border-blue-300 transition">
                  <span className="font-semibold text-gray-600 dark:text-gray-300 text-sm">{node}</span>
                  <Plus className="w-4 h-4 text-gray-400" />
                </div>
              ))}
            </div>
          </div>

          {/* Right Panel: Interactive Canvas */}
          <div className="flex-1 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-2xl p-8 relative overflow-y-auto shadow-inner flex flex-col items-center bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] dark:bg-[radial-gradient(#374151_1px,transparent_1px)] [background-size:16px_16px]">
            
            <div className="w-full max-w-2xl space-y-8 relative py-8">
              {/* Connecting Line */}
              <div className="absolute left-1/2 top-10 bottom-10 w-1 bg-gray-200 dark:bg-gray-700 -translate-x-1/2 z-0"></div>

              {nodes.map((node, index) => (
                <motion.div 
                  key={node.id}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="relative z-10 mx-auto w-80 bg-white dark:bg-gray-900 rounded-xl shadow-md border border-gray-200 dark:border-gray-700 overflow-hidden group hover:shadow-lg transition-all cursor-pointer"
                >
                  <div className={`h-1.5 w-full ${node.color}`}></div>
                  <div className="p-4 flex items-center justify-between">
                    <div>
                      <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">{node.type}</p>
                      <h3 className="text-sm font-bold text-gray-800 dark:text-gray-100">{node.name}</h3>
                    </div>
                    <div className="flex items-center gap-3">
                      {executing ? (
                         <div className="w-5 h-5 rounded-full border-2 border-blue-500 border-t-transparent animate-spin"></div>
                      ) : (
                         <div className="w-2.5 h-2.5 rounded-full bg-green-500"></div>
                      )}
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Pipelines;
