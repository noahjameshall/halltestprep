"use client";
import { useState, useEffect, Suspense } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useAuth } from "../AuthProvider";
import { getCatalog } from "@/lib/courses";

function CheckoutInner() {
  const { user, ready, grantCourse, hasCourse } = useAuth();
  const router = useRouter();
  const params = useSearchParams();
  const courseId = params.get("course") || "fe-mechanical";
  const initialPlan = params.get("plan") || "onetime";
  const canceled = params.get("canceled");
  const [plan, setPlan] = useState(initialPlan);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");

  const course = getCatalog().find((c) => c.id === courseId);

  useEffect(() => {
    if (ready && !user) {
      router.replace(`/login?next=${encodeURIComponent(`/checkout?course=${courseId}&plan=${plan}`)}`);
    }
  }, [ready, user, router, courseId, plan]);

  if (!ready || !user) return <main className="container section">Loading…</main>;
  if (!course) return <main className="container section">Course not found.</main>;

  if (hasCourse(courseId)) {
    return (
      <main className="container section narrow center">
        <div className="lock">✅</div>
        <h1>You already have access</h1>
        <p className="muted">You&apos;re enrolled in {course.title}.</p>
        <Link href={`/course/${courseId}`} className="btn lg mt">Go to the course</Link>
      </main>
    );
  }

  async function pay() {
    setLoading(true); setErr("");
    try {
      const res = await fetch("/api/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ courseId, plan, origin: window.location.origin }),
      });
      const data = await res.json();
      if (data.url) { window.location.href = data.url; return; }
      if (data.demo) {
        grantCourse(courseId, plan === "monthly" ? "subscription" : "onetime");
        router.push(`/course/${courseId}?welcome=1`);
        return;
      }
      setErr(data.error || "Something went wrong.");
    } catch (e) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="container section narrow">
      <h1>Checkout</h1>
      <p className="muted">Enrolling in <strong>{course.title}</strong></p>
      {canceled && <div className="notice mb">Your previous checkout was canceled. No charge was made.</div>}

      <div className="price-grid mt">
        <div className={`price-card ${plan === "monthly" ? "featured" : ""}`} onClick={() => setPlan("monthly")} style={{ cursor: "pointer" }}>
          <div className="flex between center-y">
            <span className="tag">Monthly</span>
            <input type="radio" checked={plan === "monthly"} onChange={() => setPlan("monthly")} />
          </div>
          <div className="amt mt">$10<span>/month</span></div>
          <p className="muted">Full access, cancel anytime.</p>
        </div>
        <div className={`price-card ${plan === "onetime" ? "featured" : ""}`} onClick={() => setPlan("onetime")} style={{ cursor: "pointer" }}>
          <div className="flex between center-y">
            <span className="tag" style={{ background: "var(--brand-soft)", color: "var(--brand)" }}>Lifetime</span>
            <input type="radio" checked={plan === "onetime"} onChange={() => setPlan("onetime")} />
          </div>
          <div className="amt mt">$100<span> once</span></div>
          <p className="muted">Pay once, keep it forever.</p>
        </div>
      </div>

      {err && <div className="error-text">{err}</div>}
      <button className="btn block lg mt-lg" onClick={pay} disabled={loading}>
        {loading ? "Processing…" : plan === "monthly" ? "Subscribe for $10/month" : "Pay $100 — lifetime access"}
      </button>
      <p className="muted center mt" style={{ fontSize: 13 }}>
        Secure checkout. You can manage or cancel your plan anytime from your account.
      </p>
    </main>
  );
}

export default function CheckoutPage() {
  return <Suspense><CheckoutInner /></Suspense>;
}
