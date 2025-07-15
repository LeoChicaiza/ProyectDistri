
import { useMutation, useQueryClient } from '@tanstack/react-query'

export function useLogin() {
  const qc = useQueryClient()
  return useMutation(
    async ({ email, password }) => {
      const res = await fetch('/auth/login', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ email, password })
      })
      if (!res.ok) throw new Error('Login fallido')
      const { access_token } = await res.json()
      localStorage.setItem('token', access_token)
      return access_token
    },
    {
      onSuccess: () => {
        // invalidamos la query 'me' para que se recargue
        qc.invalidateQueries(['me'])
      }
    }
  )
}



