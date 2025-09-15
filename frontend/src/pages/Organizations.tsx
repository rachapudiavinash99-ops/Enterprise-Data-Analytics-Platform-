import React from 'react';

const Organizations = () => {
  return (
    <div>
      <h2>Organization Management</h2>
      <button>Create Organization</button>
      <table>
        <thead>
          <tr><th>ID</th><th>Name</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>Demo Org</td></tr>
        </tbody>
      </table>
    </div>
  );
};

export default Organizations;
