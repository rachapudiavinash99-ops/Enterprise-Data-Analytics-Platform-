import React, { useState, useEffect } from 'react';
import { 
  LineChart as RechartsLineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer 
} from 'recharts';
import { Database, Settings, Loader2, ArrowUp, ArrowDown } from 'lucide-react';
import Layout from '../components/Layout';
import axios from 'axios';
import { toast } from 'react-hot-toast';

const Dashboard = () => {
  const [data, setData] = useState<{ kpis: any[], revenueTrend: any[] } | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/v1/analytics/dashboard');
        setData(res.data);
      } catch (err) {
        toast.error('Failed to load dashboard data');
      } finally {
        setLoading(false);
      }
    };
    fetchDashboard();
  }, []);

  return (
    <Layout>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-xl font-bold text-gray-800 dark:text-white">Dashboard Overview</h1>
        <div className="flex items-center gap-2 text-xs font-medium text-gray-500 bg-white dark:bg-gray-800 px-3 py-1.5 rounded-md border border-gray-200 dark:border-gray-700">
          <span className="w-2 h-2 rounded-full bg-green-500"></span>
          Data refreshed on Jun 1, 2024
        </div>
      </div>

      {loading ? (
        <div className="flex items-center justify-center h-64 bg-white rounded-lg shadow-sm border border-gray-200">
           <Loader2 className="w-8 h-8 animate-spin text-blue-600" />
        </div>
      ) : !data ? (
        <div className="text-center text-red-500 p-10 bg-white rounded-lg border border-gray-200">Failed to load data</div>
      ) : (
        <>
          <div className="grid grid-cols-4 gap-4 mb-4">
            {data.kpis.map((kpi: any, i: number) => (
              <div key={i} className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 flex flex-col justify-between">
                <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">{kpi.title}</h3>
                <span className="text-2xl font-bold text-gray-800 dark:text-white mb-2">{kpi.val}</span>
                <span className={`text-xs font-semibold flex items-center gap-1 ${kpi.up ? 'text-green-500' : 'text-red-500'}`}>
                  {kpi.up ? <ArrowUp className="w-3 h-3" /> : <ArrowDown className="w-3 h-3" />}
                  {kpi.pct} from last month
                </span>
              </div>
            ))}
          </div>

          <div className="grid grid-cols-3 gap-4">
            <div className="col-span-2 bg-white dark:bg-gray-800 p-5 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700">
              <div className="flex justify-between items-center mb-6">
                <h3 className="text-sm font-bold text-gray-800 dark:text-white">Revenue Trend</h3>
              </div>
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <RechartsLineChart data={data.revenueTrend} margin={{ top: 5, right: 20, left: -20, bottom: 0 }}>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
                    <XAxis dataKey="name" stroke="#9ca3af" tick={{fontSize: 11}} tickLine={false} axisLine={false} />
                    <YAxis stroke="#9ca3af" tick={{fontSize: 11}} tickLine={false} axisLine={false} />
                    <Tooltip contentStyle={{backgroundColor: '#1f2937', color: '#fff', borderRadius: '8px', border: 'none', fontSize: '12px'}} />
                    <Line type="monotone" dataKey="value" stroke="#2563eb" strokeWidth={2} dot={{r: 3, fill: '#2563eb'}} activeDot={{r: 5}} />
                  </RechartsLineChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="col-span-1 bg-white dark:bg-gray-800 p-5 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700">
              <h3 className="text-sm font-bold text-gray-800 dark:text-white mb-4">Top Datasets</h3>
              <div className="space-y-4">
                {[
                  { name: 'Sales Data', size: '12.4MB', icon: 'bg-blue-100 text-blue-600' },
                  { name: 'Customers', size: '6.7MB', icon: 'bg-green-100 text-green-600' },
                  { name: 'Products', size: '5.2MB', icon: 'bg-purple-100 text-purple-600' },
                  { name: 'Orders', size: '4.8MB', icon: 'bg-orange-100 text-orange-600' },
                ].map((row, i) => (
                  <div key={i} className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                       <div className={`p-1.5 rounded-md ${row.icon}`}>
                         <Database className="w-4 h-4"/>
                       </div>
                       <span className="font-semibold text-gray-700 dark:text-gray-200 text-sm">{row.name}</span>
                    </div>
                    <span className="text-xs font-medium text-gray-500">{row.size}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </>
      )}
    </Layout>
  );
};

export default Dashboard;
