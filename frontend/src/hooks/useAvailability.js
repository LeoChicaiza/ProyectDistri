import { useQuery } from '@tanstack/react-query';
import api from '../services/api';

export function useAvailability() {
  return useQuery(['availability'], () =>
    api.get('/parking/availability').then(res => res.data)
  );
}

