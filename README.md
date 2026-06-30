# HallTestPrep

A subscription test-prep platform. The flagship course is **FE Mechanical** (all 14 NCEES knowledge
areas) with, per section: a guided **Lesson**, **Practice** problems, a **Quiz**, and a **Learn & Help**
tab with fully worked solutions — plus full-length **Practice Tests**.

Built with Next.js (App Router). Accounts, enrollment, and progress work out of the box; payments are
Stripe-ready.

## Run locally
```bash
npm install
npm run dev      # http://localhost:3000
```

## How it works today (MVP)
- **Accounts & progress** are stored in the browser (localStorage). A visitor can sign up, "enroll,"
  and track progress immediately. This is per-browser, not a shared database yet — see "Going fully
  live" below.
- **Payments** run in **demo mode** unless a Stripe key is configured: checkout unlocks the course
  instantly so you can test the full experience.

## Pricing
Per course: **$10/month** (subscription) or **$100 one-time** (lifetime access to that course).
Prices live in `app/api/checkout/route.js` and the marketing copy in `app/pricing/page.js`.

## Turn on real Stripe payments
1. Create a Stripe account and grab your secret key.
2. In Vercel: Project → Settings → Environment Variables → add `STRIPE_SECRET_KEY`.
3. Redeploy. Checkout now creates real Stripe Checkout sessions ($10/mo subscription or $100 payment).

## Going fully live (recommended next steps)
The MVP keeps accounts in the browser so it can deploy with zero external setup. For real,
cross-device accounts and secure entitlements you'll want:
- A database + auth provider (e.g. Supabase, Clerk, or NextAuth + Postgres) to replace
  `app/AuthProvider.js`.
- A Stripe **webhook** that grants course access on `checkout.session.completed` (server-side),
  instead of granting on the success page.

## Add a new course
1. Create `data/course-<id>.json` (copy the FE Mechanical shape — see `gen_content.py`).
2. Register it in `lib/courses.js` and add an entry to `data/catalog.json`.
That's it — the course, section, and test pages are all data-driven.
