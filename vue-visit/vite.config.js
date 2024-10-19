import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({

  server: {
    watch: {
      usePolling: true, // Use polling instead of inotify
    },
    host: '0.0.0.0',    // Ensure the dev server listens on all network interfaces
    port: 5173,         // Ensure the port is consistent
  },
transpileDependencies: true,
  
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
