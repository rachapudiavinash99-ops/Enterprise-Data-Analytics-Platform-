import React from 'react';

const Analytics = () => {
  return (
    <div>
      <h2>Analytics Engine</h2>
      <div className='query-builder'>
        <select><option>Sales Dataset</option></select>
        <input type='text' placeholder='Group By (e.g., Region)' />
        <input type='text' placeholder='Metric (e.g., Revenue)' />
        <select><option>SUM</option><option>AVG</option></select>
        <button>Run Query</button>
      </div>
      <div className='results'>
        <p>Results will appear here...</p>
      </div>
    </div>
  );
};

export default Analytics;
