import React from 'react';
import Layout from '../components/Layout';
import { Clock, Plus } from 'lucide-react';

const Schedules = () => {
  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        <div className="flex justify-between items-end mb-8">
          <div>
            <h1 className="text-2xl font-bold text-gray-900 tracking-tight">Schedules</h1>
            <p className="text-gray-500 text-sm mt-1">Manage automated pipeline and report execution schedules.</p>
          </div>
        </div>

        <div className="bg-white border border-gray-200 rounded-2xl p-8 shadow-sm">
          <div className="flex gap-8">
            {/* Left side list */}
            <div className="w-1/3 border-r border-gray-100 pr-8">
              <button className="w-full flex items-center justify-center gap-2 bg-blue-50 text-blue-700 hover:bg-blue-100 font-semibold py-2 rounded-lg transition mb-6 border border-blue-200">
                <Plus className="w-4 h-4" /> Create Schedule
              </button>
              
              <div className="space-y-2">
                <div className="p-3 bg-blue-50 border border-blue-200 rounded-xl cursor-pointer">
                  <h4 className="font-semibold text-blue-900 text-sm">Daily Pipeline Run</h4>
                  <p className="text-xs text-blue-600 mt-1">Every day at 02:00 AM</p>
                </div>
                <div className="p-3 bg-white hover:bg-gray-50 border border-gray-100 rounded-xl cursor-pointer transition">
                  <h4 className="font-semibold text-gray-700 text-sm">Weekly Sales Report</h4>
                  <p className="text-xs text-gray-500 mt-1">Every Monday at 08:00 AM</p>
                </div>
              </div>
            </div>

            {/* Right side form */}
            <div className="flex-1 pl-4">
              <h3 className="text-lg font-bold text-gray-800 mb-6">Edit Schedule</h3>
              <div className="space-y-5">
                <div>
                  <label className="block text-xs font-semibold text-gray-500 mb-1">Schedule Name</label>
                  <input type="text" value="Daily Pipeline Run" className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2.5 text-sm text-gray-800 outline-none focus:border-blue-500" readOnly />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-semibold text-gray-500 mb-1">Pipeline</label>
                    <select className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2.5 text-sm text-gray-800 outline-none focus:border-blue-500">
                      <option>Sales ETL</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-gray-500 mb-1">Frequency</label>
                    <select className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2.5 text-sm text-gray-800 outline-none focus:border-blue-500">
                      <option>Daily</option>
                      <option>Weekly</option>
                    </select>
                  </div>
                </div>
                
                <div className="flex justify-end pt-4 gap-3">
                   <button className="px-5 py-2 text-gray-600 font-semibold hover:bg-gray-100 rounded-lg transition">Cancel</button>
                   <button className="px-5 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow-sm shadow-blue-500/20 transition">Save Schedule</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Schedules;
