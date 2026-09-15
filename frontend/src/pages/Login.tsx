import React from 'react';

const Login = () => {
  return (
    <div className='login-container'>
      <h2>Enterprise Login</h2>
      <form>
        <input type='email' placeholder='Email' />
        <input type='password' placeholder='Password' />
        <button type='submit'>Sign In</button>
      </form>
    </div>
  );
};

export default Login;
