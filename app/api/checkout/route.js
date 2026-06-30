import { NextResponse } from "next/server";

// Course pricing (server-side source of truth).
const PRICES = {
  "fe-mechanical": { name: "FE Mechanical", monthly: 1000, onetime: 10000 }, // cents
};

export async function POST(req) {
  let body = {};
  try { body = await req.json(); } catch {}
  const { courseId, plan, origin } = body;
  const price = PRICES[courseId];
  if (!price) return NextResponse.json({ error: "Unknown course" }, { status: 400 });

  const key = process.env.STRIPE_SECRET_KEY;

  // No Stripe key configured -> demo mode: the client unlocks immediately.
  if (!key) {
    return NextResponse.json({ demo: true, plan, courseId });
  }

  try {
    const Stripe = (await import("stripe")).default;
    const stripe = new Stripe(key);
    const base = origin || "";
    const isMonthly = plan === "monthly";
    const session = await stripe.checkout.sessions.create({
      mode: isMonthly ? "subscription" : "payment",
      line_items: [{
        price_data: {
          currency: "usd",
          product_data: { name: `${price.name} — ${isMonthly ? "Monthly" : "Lifetime"} access` },
          unit_amount: isMonthly ? price.monthly : price.onetime,
          ...(isMonthly ? { recurring: { interval: "month" } } : {}),
        },
        quantity: 1,
      }],
      success_url: `${base}/checkout/success?course=${courseId}&plan=${plan}`,
      cancel_url: `${base}/checkout?course=${courseId}&plan=${plan}&canceled=1`,
    });
    return NextResponse.json({ url: session.url });
  } catch (e) {
    return NextResponse.json({ error: e.message }, { status: 500 });
  }
}
