import React from 'react';

const Dashboards = () => {
  return (
    <div>
      <h2>Interactive Dashboards</h2>
      <button>Create New Dashboard</button>
      <div className='dashboard-grid' style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginTop: '20px' }}>
        <div className='widget' style={{ border: '1px solid #ccc', padding: '10px' }}>
          <h4>Total Revenue</h4>
          <h2>$1.2M</h2>
        </div>
        <div className='widget' style={{ border: '1px solid #ccc', padding: '10px' }}>
          <h4>Sales by Region</h4>
          <p>[ Bar Chart Placeholder ]</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboards;
