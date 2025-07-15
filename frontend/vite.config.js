import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      // cada ruta que empiece con /auth/ irá a tu API Gateway
      '/auth': 'http://localhost:8000',
      '/access': 'http://localhost:8000',
      '/sessions': 'http://localhost:8000',
      '/audit': 'http://localhost:8000',
      '/recovery': 'http://localhost:8000',
      '/users': 'http://localhost:8000',
      '/availability': 'http://localhost:8000',
      '/levels': 'http://localhost:8000',
      '/parking-lots': 'http://localhost:8000',
      '/slots': 'http://localhost:8000',
      '/maintenance': 'http://localhost:8000',
      '/zones': 'http://localhost:8000',
      '/ws': {
        target: 'ws://localhost:8000',
        ws: true,
      },
      '/graphql': 'http://localhost:8000',
      '/soap': 'http://localhost:8000',
      '/billing': 'http://localhost:8000'
    }
  },
  define: {
    'process.env': {}
  }
});

