# Founder to-do (only you can do these)

| # | Step | Why | Status |
|---|---|---|---|
| F1 | Send the Hyderabad office address and phone | Contact page, schema, Google Business | Waiting |
| F2 | Buy or confirm the domain (e.g. cybertronix.in) | The site needs a home | Waiting |
| F3 | Create a free Cloudflare Pages or Vercel account and connect this repo (steps below) | Hosting | Ready now: site skeleton builds |
| F4 | Google Search Console: add the domain, submit the sitemap | Google finds the site | At launch |
| F5 | Google Business Profile: category "Robotics company", address, photos, website link | #1 for "robotics in Hyderabad" | At launch |
| F6 | Same name, address, phone on LinkedIn, Justdial, IndiaMART | Google trust | After launch |
| F7 | Ask clients and partners for Google reviews | Map ranking | After launch |
| F8 | Real product photos (humanoid, arm, cleaning robot) when you have them | Replace stock | Any time |

## F3 hosting steps (pick one, both free)

**Cloudflare Pages** (recommended: free, fast in India, easy domain hookup)
1. Sign up at dash.cloudflare.com.
2. Workers & Pages → Create → Pages → Connect to Git → pick `abdulfarhath/cybertronix`.
3. Settings: Framework preset **Astro**, Root directory **`site`**, Build command **`npm run build`**, Output **`dist`**.
4. Environment variable: `NODE_VERSION` = `22`.
5. Save and deploy. Then Custom domains → add your domain (F2) and follow the DNS steps shown.
6. Tell the hub the domain, so Build can set it in `site/src/config/site-url.mjs`.

**Vercel** (alternative)
1. Sign up at vercel.com with GitHub.
2. Add New → Project → import `abdulfarhath/cybertronix`.
3. Root Directory **`site`** (framework Astro is detected). Deploy.
4. Settings → Domains → add your domain (F2) and follow the DNS steps.
5. Tell the hub the domain.

No passwords or keys go in the repo or in chat.
