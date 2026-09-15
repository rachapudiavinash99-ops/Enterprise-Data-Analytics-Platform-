import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { LineChart } from 'lucide-react';

const Login = () => {
  const [email, setEmail] = useState('admin@example.com');
  const [password, setPassword] = useState('••••••••');
  const navigate = useNavigate();

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    navigate('/');
  };

  return (
    <div className="min-h-screen bg-gray-50 flex font-sans">
      
      <div className="w-1/3 bg-[#0A192F] text-white flex flex-col justify-center px-12 relative overflow-hidden">
        <div className="absolute top-0 left-0 w-full h-full opacity-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]"></div>
        <div className="relative z-10">
          <div className="flex items-center gap-3 mb-8">
            <div className="bg-blue-600 p-2 rounded-lg">
              <LineChart className="w-6 h-6 text-white" />
            </div>
            <span className="text-xl font-bold tracking-tight">DataInsight Pro</span>
          </div>
          
          <h1 className="text-3xl font-light leading-snug mb-4">
            Turn your data into <br />
            <span className="font-bold">intelligent decisions</span>
          </h1>
          
          <div className="w-48 h-1 bg-blue-600 mt-8"></div>
        </div>
      </div>

      <div className="w-2/3 flex items-center justify-center bg-white">
        <div className="w-[400px]">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Welcome Back</h2>
          <p className="text-gray-500 text-sm mb-8">Sign in to your account to continue</p>
          
          <form onSubmit={handleLogin} className="space-y-5">
            <div>
              <label className="block text-xs font-bold text-gray-700 uppercase mb-1.5">Email address</label>
              <input 
                type="email" 
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-4 py-2.5 bg-white border border-gray-300 rounded-md text-sm text-gray-900 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors"
              />
            </div>
            <div>
              <div className="flex items-center justify-between mb-1.5">
                <label className="block text-xs font-bold text-gray-700 uppercase">Password</label>
                <a href="#" className="text-xs font-semibold text-blue-600 hover:text-blue-700">Forgot password?</a>
              </div>
              <input 
                type="password" 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-2.5 bg-white border border-gray-300 rounded-md text-sm text-gray-900 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors"
              />
            </div>

            <div className="flex items-center gap-2">
              <input type="checkbox" id="remember" className="rounded border-gray-300 text-blue-600 focus:ring-blue-500" defaultChecked />
              <label htmlFor="remember" className="text-sm font-medium text-gray-700">Remember me</label>
            </div>

            <button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-md transition-colors text-sm">
              Login
            </button>
          </form>
          
          <p className="text-center font-medium text-gray-500 text-sm mt-8">
            Don't have an account? <a href="#" className="text-blue-600 hover:text-blue-700 font-semibold">Register</a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
