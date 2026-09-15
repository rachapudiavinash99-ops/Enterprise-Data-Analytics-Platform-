import React from 'react';

const Users = () => {
  return (
    <div>
      <h2>User Management</h2>
      <button>Invite User</button>
      <table>
        <thead>
          <tr><th>Email</th><th>Role</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr><td>admin@demo.com</td><td>Admin</td><td>Active</td></tr>
        </tbody>
      </table>
    </div>
  );
};

export default Users;
