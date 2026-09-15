import React from 'react';
import Layout from '../components/Layout';
import { Activity, Search, Filter } from 'lucide-react';

const Analytics = () => {
  return (
    <Layout>
      <div className="flex flex-col h-[calc(100vh-140px)]">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 tracking-tight">Analytics Query</h1>
          <p className="text-gray-500 text-sm mt-1">Run advanced SQL and visual queries on your processed datasets.</p>
        </div>

        <div className="flex-1 flex gap-6 overflow-hidden">
          {/* Query Builder Sidebar */}
          <div className="w-80 bg-white border border-gray-200 rounded-2xl p-5 overflow-y-auto shadow-sm flex flex-col">
            <h3 className="text-sm font-bold text-gray-800 mb-4 flex items-center gap-2"><Filter className="w-4 h-4"/> Query Builder</h3>
            
            <div className="space-y-4 flex-1">
              <div>
                <label className="block text-xs font-semibold text-gray-500 mb-1">Dataset</label>
                <select className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2 text-sm text-gray-700 outline-none focus:border-blue-500">
                  <option>Sales Data</option>
                  <option>Customer Churn</option>
                </select>
              </div>
              <div>
                <label className="block text-xs font-semibold text-gray-500 mb-1">Group By</label>
                <select className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2 text-sm text-gray-700 outline-none focus:border-blue-500">
                  <option>Region</option>
                  <option>Product Category</option>
                </select>
              </div>
              <div>
                <label className="block text-xs font-semibold text-gray-500 mb-1">Metric</label>
                <select className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2 text-sm text-gray-700 outline-none focus:border-blue-500">
                  <option>Revenue</option>
                  <option>Orders Count</option>
                </select>
              </div>
              <div>
                <label className="block text-xs font-semibold text-gray-500 mb-1">Aggregation</label>
                <select className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2 text-sm text-gray-700 outline-none focus:border-blue-500">
                  <option>SUM</option>
                  <option>AVERAGE</option>
                </select>
              </div>
            </div>
            
            <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2.5 rounded-xl transition shadow-md shadow-blue-500/20 flex justify-center items-center gap-2">
              <Activity className="w-4 h-4" /> Run Query
            </button>
          </div>

          {/* Results Area */}
          <div className="flex-1 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm overflow-auto">
            <h3 className="text-base font-bold text-gray-800 mb-6">Results</h3>
            
            <table className="w-full text-left text-sm">
              <thead className="text-xs text-gray-500 uppercase border-b border-gray-100">
                <tr>
                  <th className="pb-3 font-semibold">Region</th>
                  <th className="pb-3 font-semibold text-right">Total Revenue</th>
                  <th className="pb-3 font-semibold w-1/3"></th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-50">
                {[
                  { region: 'North', val: '450,230', pct: '85%' },
                  { region: 'South', val: '382,120', pct: '70%' },
                  { region: 'East', val: '280,450', pct: '55%' },
                  { region: 'West', val: '210,890', pct: '40%' },
                ].map((row, i) => (
                  <tr key={i}>
                    <td className="py-4 font-medium text-gray-800">{row.region}</td>
                    <td className="py-4 text-right font-semibold text-gray-700">{row.val}</td>
                    <td className="py-4 pl-8">
                      <div className="w-full bg-gray-100 h-2 rounded-full overflow-hidden">
                        <div className="bg-blue-500 h-full rounded-full" style={{ width: row.pct }}></div>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Analytics;
