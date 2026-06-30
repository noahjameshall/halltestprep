"use client";
import { useState, Suspense } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useAuth } from "../AuthProvider";

function LoginInner() {
  const { login } = useAuth();
  const router = useRouter();
  const params = useSearchParams();
  const next = params.get("next") || "/dashboard";
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");

  function submit(e) {
    e.preventDefault();
    setErr("");
    const r = login(email, password);
    if (!r.ok) { setErr(r.error); return; }
    router.push(next);
  }

  return (
    <div className="auth-wrap">
      <div className="card auth-card pad-lg">
        <h2>Welcome back</h2>
        <p className="muted" style={{ marginTop: -6 }}>Log in to continue your prep.</p>
        <form onSubmit={submit}>
          <div className="field"><label>Email</label><input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="you@example.com" /></div>
          <div className="field"><label>Password</label><input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="••••••••" /></div>
          {err && <div className="error-text">{err}</div>}
          <button className="btn block lg mt" type="submit">Log in</button>
        </form>
        <p className="muted mt">New here? <Link href="/signup" style={{ color: "var(--brand)", fontWeight: 600 }}>Create an account</Link></p>
      </div>
    </div>
  );
}

export default function LoginPage() {
  return <Suspense><LoginInner /></Suspense>;
}
