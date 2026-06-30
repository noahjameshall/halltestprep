import Link from "next/link";

export default function Pricing() {
  return (
    <main className="container section narrow">
      <div className="center mb">
        <h1>Simple, per-course pricing</h1>
        <p className="muted">Choose the plan that fits how you study. Cancel the monthly plan anytime.</p>
      </div>
      <div className="price-grid">
        <div className="price-card">
          <span className="tag">Most flexible</span>
          <div className="amt mt">$10<span>/month</span></div>
          <p className="muted">Per course. Great if your exam is soon and you want full access now.</p>
          <ul className="checklist">
            <li>All lessons, problems &amp; quizzes</li>
            <li>Full-length practice tests</li>
            <li>Learn &amp; Help worked solutions</li>
            <li>Progress tracking</li>
            <li>Cancel anytime</li>
          </ul>
          <Link href="/checkout?course=fe-mechanical&plan=monthly" className="btn block lg">Start monthly</Link>
        </div>
        <div className="price-card featured">
          <span className="tag" style={{ background: "var(--brand-soft)", color: "var(--brand)" }}>Best value</span>
          <div className="amt mt">$100<span> once</span></div>
          <p className="muted">Per course. Pay once, keep lifetime access. Cheaper if you study for 10+ months.</p>
          <ul className="checklist">
            <li>Everything in monthly</li>
            <li>Lifetime access to this course</li>
            <li>All future updates to the course</li>
            <li>No recurring charges</li>
          </ul>
          <Link href="/checkout?course=fe-mechanical&plan=onetime" className="btn block lg">Buy lifetime access</Link>
        </div>
      </div>
      <p className="muted center mt-lg" style={{ fontSize: 13 }}>
        Pricing is per course. Each course you enroll in is billed separately.
      </p>
    </main>
  );
}
