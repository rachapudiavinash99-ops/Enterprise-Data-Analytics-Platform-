import React from 'react';

const Pipelines = () => {
  return (
    <div>
      <h2>Visual Pipeline Builder</h2>
      <div style={{ display: 'flex', gap: '20px' }}>
        <div className='nodes-panel'>
          <h4>Nodes</h4>
          <ul>
            <li>Input</li>
            <li>Clean</li>
            <li>Transform</li>
            <li>Output</li>
          </ul>
        </div>
        <div className='canvas' style={{ border: '1px solid black', width: '600px', height: '400px' }}>
          <p style={{ textAlign: 'center', marginTop: '180px' }}>Canvas Area</p>
        </div>
      </div>
    </div>
  );
};

export default Pipelines;
