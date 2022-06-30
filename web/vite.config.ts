import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    hmr: {
      protocol: "ws",
      host: "127.0.0.1",      
    },
    watch: {
      usePolling: true
    }
  }
});
