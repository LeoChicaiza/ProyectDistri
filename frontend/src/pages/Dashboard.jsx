// src/pages/Dashboard.jsx
import React, { useEffect, useState } from 'react';
import { getSessions }               from '../services/api';

export default function Dashboard({ user }) {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    getSessions(user.user_id)
      .then(data => setSessions(data.value))
      .catch(console.error);
  }, [user]);

  return (
    <div>
      <h2 className="text-2xl">Welcome, {user.email}</h2>
      <h3>Active Sessions</h3>
      <ul>
        {sessions.map(s => (
          <li key={s.session_id}>
            {s.ip_address} @ {new Date(s.login_time).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
}


