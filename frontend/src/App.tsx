import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Organizations from './pages/Organizations';
import Users from './pages/Users';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/login' element={<Login />} />
        <Route path='/' element={<Dashboard />} />
        <Route path='/organizations' element={<Organizations />} />
        <Route path='/users' element={<Users />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
