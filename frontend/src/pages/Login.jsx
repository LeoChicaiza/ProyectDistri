import React, { useState } from 'react';
import { useLogin } from '../hooks/useAuth';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const login = useLogin();
  const nav = useNavigate();

  const handleSubmit = e => {
    e.preventDefault();
    login.mutate({ email, password }, {
      onSuccess: () => nav('/dashboard'),
    });
  };

  return (
    <div className="max-w-sm mx-auto mt-20 p-6 bg-white shadow rounded">
      <h2 className="text-2xl font-bold mb-4">Login</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          className="w-full px-3 py-2 border rounded"
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          className="w-full px-3 py-2 border rounded"
          required
        />
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded disabled:opacity-50"
          disabled={login.isLoading}
        >
          {login.isLoading ? 'Logging in…' : 'Login'}
        </button>
        {login.isError && (
          <p className="text-red-600">Login failed. Check your credentials.</p>
        )}
      </form>
    </div>
  );
}

