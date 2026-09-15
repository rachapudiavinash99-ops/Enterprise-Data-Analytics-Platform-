import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Toaster, toast } from 'react-hot-toast';
import { 
  LayoutDashboard, Database, Activity, GitBranch, Bell, Settings,
  Search, Moon, Sun, ChevronDown, FileText, Clock, LogOut, Hexagon,
  LineChart
} from 'lucide-react';

const Layout = ({ children }: { children: React.ReactNode }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const handleNav = (path: string) => navigate(path);

  const navItems = [
    { name: 'Dashboard', icon: <LayoutDashboard className="w-4 h-4" />, path: '/' },
    { name: 'Datasets', icon: <Database className="w-4 h-4" />, path: '/datasets' },
    { name: 'Pipelines', icon: <GitBranch className="w-4 h-4" />, path: '/pipelines' },
    { name: 'Analytics', icon: <Activity className="w-4 h-4" />, path: '/analytics' },
    { name: 'Reports', icon: <FileText className="w-4 h-4" />, path: '/reports' },
    { name: 'Schedules', icon: <Clock className="w-4 h-4" />, path: '/schedules' },
    { name: 'Alerts', icon: <Bell className="w-4 h-4" />, path: '/alerts' },
    { name: 'Settings', icon: <Settings className="w-4 h-4" />, path: '/settings' },
  ];

  return (
    <div className={`flex h-screen overflow-hidden font-sans ${darkMode ? 'bg-gray-900 text-white' : 'bg-[#f4f7f6] text-gray-900'}`}>
      <Toaster position="top-right" />
      
      {/* Sidebar - DataInsight Pro Style */}
      <div className="w-[240px] bg-[#0A192F] text-gray-300 flex flex-col flex-shrink-0 min-h-screen shadow-xl z-20 transition-colors">
        <div className="h-16 flex items-center px-6 gap-3 border-b border-white/10 bg-[#061122]">
          <div className="bg-blue-600 p-1.5 rounded-lg">
            <LineChart className="w-5 h-5 text-white" />
          </div>
          <span className="text-white font-bold text-lg tracking-tight">DataInsight Pro</span>
        </div>
        
        <div className="flex-1 py-4 overflow-y-auto">
          <nav className="space-y-1 px-3">
            {navItems.map((item) => {
              const isActive = location.pathname === item.path || (location.pathname !== '/' && item.path !== '/' && location.pathname.startsWith(item.path));
              return (
                <button 
                  key={item.name}
                  onClick={() => handleNav(item.path)} 
                  className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-md transition font-medium text-sm ${
                    isActive 
                      ? 'bg-blue-600 text-white' 
                      : 'text-gray-400 hover:bg-white/5 hover:text-white'
                  }`}
                >
                  {item.icon} {item.name}
                </button>
              );
            })}
          </nav>
        </div>

        <div className="p-4 border-t border-white/10">
           <button onClick={() => { localStorage.clear(); toast.success('Signed out successfully'); navigate('/login'); }} className="w-full flex items-center gap-3 text-gray-400 hover:text-white hover:bg-white/5 px-3 py-2.5 rounded-md transition font-medium text-sm">
             <LogOut className="w-4 h-4" /> Sign Out
           </button>
        </div>
      </div>
      
      {/* Main Content Wrapper */}
      <div className="flex-1 flex flex-col min-w-0 z-10">
        {/* TopBar */}
        <div className={`h-16 border-b flex items-center justify-between px-8 flex-shrink-0 shadow-sm transition-colors ${darkMode ? 'bg-gray-800 border-gray-700' : 'bg-white border-gray-200'}`}>
          <div className="flex-1 flex items-center">
            <div className="relative w-96 group">
              <Search className="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input type="text" placeholder="Search anything..." className={`w-full pl-10 pr-4 py-1.5 border rounded-md text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 transition-all ${darkMode ? 'bg-gray-900 border-gray-700 text-white' : 'bg-gray-50 border-gray-300 text-gray-900 focus:bg-white'}`} />
            </div>
          </div>
          <div className="flex items-center gap-4">
            <div className={`flex items-center gap-1 p-1 rounded-full border ${darkMode ? 'bg-gray-900 border-gray-700' : 'bg-gray-100 border-gray-200'}`}>
              <button onClick={() => setDarkMode(false)} className={`p-1 rounded-full transition ${!darkMode ? 'bg-white text-gray-700 shadow-sm' : 'text-gray-500'}`}><Sun className="w-4 h-4" /></button>
              <button onClick={() => setDarkMode(true)} className={`p-1 rounded-full transition ${darkMode ? 'bg-gray-700 text-white shadow-sm' : 'text-gray-500'}`}><Moon className="w-4 h-4" /></button>
            </div>
            <button className="text-gray-400 hover:text-gray-600 relative">
               <Bell className="w-5 h-5" />
               <span className="absolute -top-0.5 -right-0.5 w-2 h-2 bg-red-500 rounded-full border-2 border-white"></span>
            </button>
            <div className="w-px h-6 bg-gray-300 mx-2"></div>
            <div className="flex items-center gap-3 cursor-pointer">
              <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-sm">A</div>
              <div className="text-sm hidden md:block">
                <p className={`font-bold leading-none mb-0.5 ${darkMode ? 'text-white' : 'text-gray-700'}`}>Admin</p>
                <p className="text-[10px] text-gray-500">Super Admin</p>
              </div>
              <ChevronDown className="w-4 h-4 text-gray-400" />
            </div>
          </div>
        </div>
        
        {/* Page Content */}
        <div className="flex-1 overflow-auto p-6">
           {children}
        </div>
      </div>
    </div>
  );
};

export default Layout;
