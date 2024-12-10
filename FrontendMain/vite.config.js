import { defineConfig } from 'vite'

import react from '@vitejs/plugin-react'

  

// https://vitejs.dev/config/

export default defineConfig({
  plugins: [react()],
  // The line below is compulsory if you want to add your custom models
  assetsInclude: ['src/**/*.gltf', '*src/**/*.glb'],

})