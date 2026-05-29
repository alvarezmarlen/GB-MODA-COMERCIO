import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/stories': 'http://backend:5000',
      '/uploads': 'http://backend:5000',
      '/users': 'http://backend:5000',
      '/auth': 'http://backend:5000',
    }
  }
})
