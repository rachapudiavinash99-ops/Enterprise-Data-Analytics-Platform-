import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Organizations from './pages/Organizations';
import Users from './pages/Users';
import Datasets from './pages/Datasets';
import DataQuality from './pages/DataQuality';
import Pipelines from './pages/Pipelines';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/login' element={<Login />} />
        <Route path='/' element={<Dashboard />} />
        <Route path='/organizations' element={<Organizations />} />
        <Route path='/users' element={<Users />} />
        <Route path='/datasets' element={<Datasets />} />
        <Route path='/quality' element={<DataQuality />} />
        <Route path='/pipelines' element={<Pipelines />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
