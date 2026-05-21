import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/stories': 'http://localhost:5000',
      '/uploads': 'http://localhost:5000',
      '/users': 'http://localhost:5000',
    }
  }
})
