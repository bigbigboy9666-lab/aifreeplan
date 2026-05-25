// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
  site: 'https://aifreeplan.com',
  output: 'static',
  adapter: cloudflare(),

  i18n: {
    locales: ['zh', 'en'],
    defaultLocale: 'zh',
    routing: {
      prefixDefaultLocale: true,
    },
  },

  build: {
    format: 'file',
  },

  trailingSlash: 'never',

  vite: {
    resolve: {
      alias: {
        '@': '/src',
      },
    },
  },
});
