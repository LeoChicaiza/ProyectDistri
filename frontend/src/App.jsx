// src/App.jsx
import { Routes, Route, Navigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getMe } from './services/api'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'

export default function App() {
 
  const { data: me, isLoading, isError } = useQuery({
    queryKey: ['me'],     
    queryFn: () => getMe(), 
  })

  if (isLoading) return <p>Cargando…</p>
  if (isError)   return <p>Error comprobando sesión</p>

  return (
    <Routes>
      <Route
        path="/login"
        element={me ? <Navigate to="/dashboard" /> : <Login />}
      />
      <Route
        path="/dashboard"
        element={me ? <Dashboard /> : <Navigate to="/login" />}
      />
      {/* redirige la raíz */}
      <Route
        path="/"
        element={<Navigate to={me ? "/dashboard" : "/login"} replace />}
      />
      <Route path="*" element={<p>404: Página no encontrada</p>} />
    </Routes>
  )
}

