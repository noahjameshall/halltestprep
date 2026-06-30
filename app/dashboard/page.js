"use client";
import { useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../AuthProvider";
import { getCatalog, getCourse, courseStats } from "@/lib/courses";

export default function Dashboard() {
  const { user, ready, hasCourse, getProgress } = useAuth();
  const router = useRouter();
  const courses = getCatalog();

  useEffect(() => {
    if (ready && !user) router.replace("/login?next=/dashboard");
  }, [ready, user, router]);

  if (!ready || !user) return <main className="container section">Loading…</main>;

  const enrolled = courses.filter((c) => c.status === "available" && hasCourse(c.id));
  const browse = courses.filter((c) => !(c.status === "available" && hasCourse(c.id)));

  return (
    <main className="container section">
      <h1>Welcome back, {user.name} 👋</h1>
      <p className="muted">Pick up where you left off, or enroll in a new course.</p>

      <h2 className="mt-lg">My courses</h2>
      {enrolled.length === 0 ? (
        <div className="card">
          <p style={{ margin: 0 }}>You haven&apos;t enrolled in any courses yet.</p>
          <Link href="/course/fe-mechanical" className="btn mt">Browse FE Mechanical</Link>
        </div>
      ) : (
        <div className="grid cols-3">
          {enrolled.map((c) => {
            const course = getCourse(c.id);
            const stats = courseStats(c.id);
            const prog = getProgress(c.id);
            const done = course ? course.sections.filter((s) => prog[s.id]).length : 0;
            const pct = stats ? Math.round((done / stats.sections) * 100) : 0;
            return (
              <Link key={c.id} href={`/course/${c.id}`} className="card course-card">
                <div className="bar" style={{ background: c.color }} />
                <div className="flex between center-y">
                  <h3 style={{ margin: 0 }}>{c.title}</h3>
                  <span className="badge owned">Enrolled</span>
                </div>
                <div className="muted" style={{ fontSize: 14 }}>{done} of {stats.sections} sections complete</div>
                <div className="progress"><span style={{ width: `${pct}%` }} /></div>
                <div style={{ marginTop: "auto", paddingTop: 8, fontWeight: 650, color: c.color }}>Continue →</div>
              </Link>
            );
          })}
        </div>
      )}

      <h2 className="mt-lg">Explore more</h2>
      <div className="grid cols-3">
        {browse.map((c) => {
          const available = c.status === "available";
          const Wrapper = available ? Link : "div";
          return (
            <Wrapper key={c.id} href={available ? `/course/${c.id}` : "#"} className="card course-card" style={{ opacity: available ? 1 : 0.75 }}>
              <div className="bar" style={{ background: c.color }} />
              <div className="flex between center-y">
                <h3 style={{ margin: 0 }}>{c.title}</h3>
                {available ? <span className="badge live">Available</span> : <span className="badge soon">Coming soon</span>}
              </div>
              <p className="muted" style={{ margin: 0 }}>{c.blurb}</p>
              {available && <div style={{ marginTop: "auto", paddingTop: 8, fontWeight: 650, color: c.color }}>Enroll →</div>}
            </Wrapper>
          );
        })}
      </div>
    </main>
  );
}
