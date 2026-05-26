import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/stories': 'http://localhost:5002',
      '/uploads': 'http://localhost:5002',
      '/users': 'http://localhost:5002',
      '/auth': 'http://localhost:5002',
    }
  }
})
