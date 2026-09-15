import React from 'react';
import Layout from '../components/Layout';
import { Bell, ShieldAlert, CheckCircle2 } from 'lucide-react';

const Alerts = () => {
  return (
    <Layout>
      <div className="max-w-5xl mx-auto">
        <div className="flex justify-between items-end mb-8">
          <div>
            <h1 className="text-2xl font-bold text-gray-900 tracking-tight">Alerts & Notifications</h1>
            <p className="text-gray-500 text-sm mt-1">Configure automated alerts for data quality issues or metric drops.</p>
          </div>
          <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded-lg transition shadow-sm shadow-blue-500/20">
            Create Alert
          </button>
        </div>

        <div className="bg-white border border-gray-200 rounded-2xl shadow-sm overflow-hidden">
          <table className="w-full text-left text-sm">
            <thead className="text-xs text-gray-500 uppercase border-b border-gray-100 bg-gray-50/50">
              <tr>
                <th className="px-6 py-4 font-semibold">Name</th>
                <th className="px-6 py-4 font-semibold">Condition</th>
                <th className="px-6 py-4 font-semibold">Status</th>
                <th className="px-6 py-4 font-semibold text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-50 text-gray-700">
              <tr>
                <td className="px-6 py-4 font-medium flex items-center gap-2"><Bell className="w-4 h-4 text-blue-500"/> Low Revenue Alert</td>
                <td className="px-6 py-4">Revenue &lt; 50000</td>
                <td className="px-6 py-4"><span className="bg-green-100 text-green-700 px-2.5 py-1 rounded-md text-xs font-bold flex items-center gap-1 w-max"><CheckCircle2 className="w-3 h-3"/> Active</span></td>
                <td className="px-6 py-4 text-right">
                  <div className="w-10 h-5 bg-blue-600 rounded-full relative inline-block cursor-pointer"><div className="w-3 h-3 bg-white rounded-full absolute top-1 right-1"></div></div>
                </td>
              </tr>
              <tr>
                <td className="px-6 py-4 font-medium flex items-center gap-2"><ShieldAlert className="w-4 h-4 text-red-500"/> Pipeline Failure Alert</td>
                <td className="px-6 py-4">On Failure</td>
                <td className="px-6 py-4"><span className="bg-green-100 text-green-700 px-2.5 py-1 rounded-md text-xs font-bold flex items-center gap-1 w-max"><CheckCircle2 className="w-3 h-3"/> Active</span></td>
                <td className="px-6 py-4 text-right">
                  <div className="w-10 h-5 bg-blue-600 rounded-full relative inline-block cursor-pointer"><div className="w-3 h-3 bg-white rounded-full absolute top-1 right-1"></div></div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </Layout>
  );
};

export default Alerts;
