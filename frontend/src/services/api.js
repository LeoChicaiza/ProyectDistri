
const API_URL = '/'; 

export async function login({ email, password }) {
  const res = await fetch(`${API_URL}auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) throw new Error((await res.json()).detail || 'Login failed');
  return res.json(); // { access_token }
}

function getAuthHeaders() {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}

export async function getMe() {
  const res = await fetch(`${API_URL}users/me`, {
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeaders(),
    },
  });
  if (!res.ok) throw new Error('Unauthorized');
  return res.json();
}


export async function getSessions(userId) {
  const res = await fetch(`${API_URL}sessions/user/${userId}`, {
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) throw new Error('Failed to fetch sessions');
  return res.json(); // { value: [...], Count }
}


