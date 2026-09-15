import React, { useState } from 'react';

const Datasets = () => {
  const [uploading, setUploading] = useState(false);
  
  const handleUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setUploading(true);
      // Mock upload delay
      setTimeout(() => setUploading(false), 2000);
    }
  };

  return (
    <div>
      <h2>Dataset Management</h2>
      <input type='file' accept='.csv,.xlsx,.json' onChange={handleUpload} />
      {uploading && <p>Uploading...</p>}
      <table>
        <thead>
          <tr><th>Name</th><th>Rows</th><th>Size</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr><td>sales_data.csv</td><td>10,000</td><td>2.5 MB</td><td>Profiled</td></tr>
        </tbody>
      </table>
    </div>
  );
};

export default Datasets;
