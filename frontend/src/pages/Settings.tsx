import React from 'react';
import Layout from '../components/Layout';
import { User, Shield, Key, Bell } from 'lucide-react';

const Settings = () => {
  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        <div className="mb-8">
          <h1 className="text-2xl font-bold text-gray-900 tracking-tight">Settings</h1>
          <p className="text-gray-500 text-sm mt-1">Manage your account and platform preferences.</p>
        </div>

        <div className="bg-white border border-gray-200 rounded-2xl p-8 shadow-sm flex gap-8">
          
          <div className="w-48 space-y-2 border-r border-gray-100 pr-6">
            <button className="w-full text-left px-3 py-2 bg-blue-50 text-blue-700 font-semibold rounded-lg flex items-center gap-2"><User className="w-4 h-4"/> Profile</button>
            <button className="w-full text-left px-3 py-2 text-gray-600 hover:bg-gray-50 font-medium rounded-lg flex items-center gap-2 transition"><Shield className="w-4 h-4"/> Security</button>
            <button className="w-full text-left px-3 py-2 text-gray-600 hover:bg-gray-50 font-medium rounded-lg flex items-center gap-2 transition"><Key className="w-4 h-4"/> API Keys</button>
            <button className="w-full text-left px-3 py-2 text-gray-600 hover:bg-gray-50 font-medium rounded-lg flex items-center gap-2 transition"><Bell className="w-4 h-4"/> Notifications</button>
          </div>

          <div className="flex-1">
             <h3 className="text-lg font-bold text-gray-800 mb-6">Profile Settings</h3>
             <div className="flex items-center gap-6 mb-8">
               <div className="w-20 h-20 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 text-2xl font-bold border-2 border-blue-200">A</div>
               <div>
                 <button className="px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-semibold text-gray-700 hover:bg-gray-50 mb-2">Change Avatar</button>
                 <p className="text-xs text-gray-500">JPG, GIF or PNG. Max size of 800K</p>
               </div>
             </div>

             <div className="grid grid-cols-2 gap-6 mb-6">
               <div>
                 <label className="block text-xs font-semibold text-gray-500 mb-1">First Name</label>
                 <input type="text" value="Admin" className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2.5 text-sm text-gray-800 outline-none focus:border-blue-500" readOnly />
               </div>
               <div>
                 <label className="block text-xs font-semibold text-gray-500 mb-1">Last Name</label>
                 <input type="text" value="User" className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2.5 text-sm text-gray-800 outline-none focus:border-blue-500" readOnly />
               </div>
               <div className="col-span-2">
                 <label className="block text-xs font-semibold text-gray-500 mb-1">Email Address</label>
                 <input type="text" value="admin@example.com" className="w-full bg-gray-50 border border-gray-200 rounded-lg p-2.5 text-sm text-gray-800 outline-none focus:border-blue-500" readOnly />
               </div>
             </div>
             
             <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2.5 rounded-lg transition shadow-sm shadow-blue-500/20">
                Save Changes
             </button>
          </div>

        </div>
      </div>
    </Layout>
  );
};

export default Settings;
