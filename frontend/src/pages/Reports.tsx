import React from 'react';
import Layout from '../components/Layout';
import { Download, FileText, ChevronRight } from 'lucide-react';

const Reports = () => {
  return (
    <Layout>
      <div className="max-w-5xl mx-auto">
        <div className="flex justify-between items-end mb-8">
          <div>
            <h1 className="text-2xl font-bold text-gray-900 tracking-tight">Report Generation & Export</h1>
            <p className="text-gray-500 text-sm mt-1">Generate, view, and export formatted business reports.</p>
          </div>
          <button className="flex items-center gap-2 bg-blue-50 text-blue-700 border border-blue-200 hover:bg-blue-100 font-semibold px-4 py-2 rounded-lg transition">
            <Download className="w-4 h-4" /> Export PDF
          </button>
        </div>

        <div className="bg-white border border-gray-200 rounded-2xl p-8 shadow-sm">
           <div className="border-b border-gray-100 pb-6 mb-6">
             <h2 className="text-xl font-bold text-gray-800">Sales Performance Report</h2>
             <p className="text-sm text-gray-500 mt-1">Generated on: 2024-06-01 10:30 | Organization: Acme Corp</p>
           </div>
           
           <h3 className="text-sm font-bold text-gray-700 uppercase tracking-widest mb-4">Key Metrics</h3>
           <div className="grid grid-cols-3 gap-6 mb-10">
             <div className="bg-gray-50 p-4 rounded-xl border border-gray-100">
               <p className="text-xs font-semibold text-gray-500 mb-1">Total Revenue</p>
               <p className="text-2xl font-bold text-gray-900">$1,248,230</p>
             </div>
             <div className="bg-gray-50 p-4 rounded-xl border border-gray-100">
               <p className="text-xs font-semibold text-gray-500 mb-1">Total Orders</p>
               <p className="text-2xl font-bold text-gray-900">8,532</p>
             </div>
             <div className="bg-gray-50 p-4 rounded-xl border border-gray-100">
               <p className="text-xs font-semibold text-gray-500 mb-1">Profit Margin</p>
               <p className="text-2xl font-bold text-gray-900">24.8%</p>
             </div>
           </div>

           <div className="space-y-3">
             <div className="flex items-center justify-between p-4 bg-gray-50 rounded-xl border border-gray-100 cursor-pointer hover:bg-gray-100 transition">
               <div className="flex items-center gap-3">
                 <FileText className="w-5 h-5 text-blue-500" />
                 <span className="font-semibold text-gray-700">Q1 Financial Summary</span>
               </div>
               <ChevronRight className="w-4 h-4 text-gray-400" />
             </div>
             <div className="flex items-center justify-between p-4 bg-gray-50 rounded-xl border border-gray-100 cursor-pointer hover:bg-gray-100 transition">
               <div className="flex items-center gap-3">
                 <FileText className="w-5 h-5 text-blue-500" />
                 <span className="font-semibold text-gray-700">Annual Customer Churn Report</span>
               </div>
               <ChevronRight className="w-4 h-4 text-gray-400" />
             </div>
           </div>
        </div>
      </div>
    </Layout>
  );
};

export default Reports;
