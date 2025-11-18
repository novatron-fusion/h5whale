import react from '@vitejs/plugin-react-swc';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    react({
      swcOptions: {
        minify: false,
      },
    }),
  ],
  build: {
    minify: false,
    sourcemap: true,
  },
  preview: {
    allowedHosts: ['all'],
  },
});
