import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  assetsInclude: ['src/**/*.gltf', '*src/**/*.glb','**/*.glb','*public/**/*.gltf'],
})