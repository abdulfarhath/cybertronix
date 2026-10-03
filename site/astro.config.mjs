// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { SITE_URL } from './src/config/site-url.mjs';

// Clean URLs: /robotic-arm (no trailing slash, no .html).
// build.format 'file' writes robotic-arm.html, which Cloudflare Pages and Vercel (cleanUrls) serve at /robotic-arm.
export default defineConfig({
  site: SITE_URL,
  trailingSlash: 'never',
  build: { format: 'file', inlineStylesheets: 'always' },
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/404'),
    }),
  ],
});
