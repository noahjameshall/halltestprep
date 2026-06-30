"use client";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "./AuthProvider";

export default function Nav() {
  const { user, logout, ready } = useAuth();
  const router = useRouter();
  return (
    <nav className="nav">
      <div className="container nav-inner">
        <Link href="/" className="brand">
          <span className="mark"><small>H</small></span>
          <span>HallTestPrep</span>
        </Link>
        <div className="nav-links">
          <Link href="/#courses" className="btn ghost hide-mobile">Courses</Link>
          <Link href="/pricing" className="btn ghost hide-mobile">Pricing</Link>
          {ready && user ? (
            <>
              <Link href="/dashboard" className="btn secondary">My Courses</Link>
              <button className="btn ghost" onClick={() => { logout(); router.push("/"); }}>Log out</button>
            </>
          ) : ready ? (
            <>
              <Link href="/login" className="btn ghost">Log in</Link>
              <Link href="/signup" className="btn">Get started</Link>
            </>
          ) : null}
        </div>
      </div>
    </nav>
  );
}
