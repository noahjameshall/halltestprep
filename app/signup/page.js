"use client";
import { useState, Suspense } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useAuth } from "../AuthProvider";

function SignupInner() {
  const { signup } = useAuth();
  const router = useRouter();
  const params = useSearchParams();
  const next = params.get("next") || "/dashboard";
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");

  function submit(e) {
    e.preventDefault();
    setErr("");
    if (!email || !password) { setErr("Email and password are required."); return; }
    if (password.length < 4) { setErr("Use a password of at least 4 characters."); return; }
    const r = signup(email, password, name);
    if (!r.ok) { setErr(r.error); return; }
    router.push(next);
  }

  return (
    <div className="auth-wrap">
      <div className="card auth-card pad-lg">
        <h2>Create your account</h2>
        <p className="muted" style={{ marginTop: -6 }}>Start studying in under a minute.</p>
        <form onSubmit={submit}>
          <div className="field"><label>Name</label><input value={name} onChange={(e) => setName(e.target.value)} placeholder="Noah Hall" /></div>
          <div className="field"><label>Email</label><input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="you@example.com" /></div>
          <div className="field"><label>Password</label><input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="••••••••" /></div>
          {err && <div className="error-text">{err}</div>}
          <button className="btn block lg mt" type="submit">Create account</button>
        </form>
        <p className="muted mt">Already have an account? <Link href="/login" style={{ color: "var(--brand)", fontWeight: 600 }}>Log in</Link></p>
      </div>
    </div>
  );
}

export default function SignupPage() {
  return <Suspense><SignupInner /></Suspense>;
}
