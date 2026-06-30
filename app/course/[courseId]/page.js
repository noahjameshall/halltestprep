"use client";
import Link from "next/link";
import { useAuth } from "../../AuthProvider";
import { getCourse, courseStats } from "@/lib/courses";

export default function CourseOverview({ params }) {
  const { courseId } = params;
  const { user, ready, hasCourse, getProgress } = useAuth();
  const course = getCourse(courseId);
  const stats = courseStats(courseId);

  if (!course) return <main className="container section">Course not found.</main>;

  const owned = ready && user && hasCourse(courseId);
  const prog = owned ? getProgress(courseId) : {};
  const enrollHref = user ? `/checkout?course=${courseId}&plan=onetime` : `/signup?next=${encodeURIComponent(`/checkout?course=${courseId}`)}`;

  return (
    <main>
      <section className="hero" style={{ padding: "56px 0 64px" }}>
        <div className="container">
          <div className="eyebrow">{course.subtitle}</div>
          <h1 style={{ marginBottom: 10 }}>{course.title}</h1>
          <p className="lead">{course.tagline}</p>
          <div className="hero-stats" style={{ marginTop: 28 }}>
            <div className="stat"><div className="n">{course.examFacts.questions}</div><div className="l">Exam questions</div></div>
            <div className="stat"><div className="n">{course.examFacts.hours} hrs</div><div className="l">Appointment</div></div>
            <div className="stat"><div className="n">{stats.sections}</div><div className="l">Knowledge areas</div></div>
            <div className="stat"><div className="n">{stats.totalQuestions}+</div><div className="l">Practice questions</div></div>
          </div>
          <div className="hero-cta">
            {owned ? (
              <Link href={`/course/${courseId}/section/${course.sections[0].id}`} className="btn lg">Start the first lesson</Link>
            ) : (
              <>
                <Link href={enrollHref} className="btn lg">Enroll — $100 lifetime</Link>
                <Link href={`/checkout?course=${courseId}&plan=monthly`} className="btn lg secondary">or $10/month</Link>
              </>
            )}
          </div>
        </div>
      </section>

      <div className="container course-shell">
        <aside className="sidebar">
          <div className="sb-title">Course content</div>
          {course.sections.map((s, i) => {
            const done = !!prog[s.id];
            const inner = (
              <div className={`sb-item ${done ? "done" : ""}`}>
                <span><span className="dot" /> {s.title}</span>
              </div>
            );
            return owned
              ? <Link key={s.id} href={`/course/${courseId}/section/${s.id}`}>{inner}</Link>
              : <div key={s.id} title="Enroll to unlock">{inner}</div>;
          })}
          <div className="sb-title mt">Practice tests</div>
          {course.practiceTests.map((t) => {
            const inner = <div className="sb-item"><span>📝 {t.title.replace(/Practice Test \d+ - /, "")}</span></div>;
            return owned ? <Link key={t.id} href={`/course/${courseId}/test/${t.id}`}>{inner}</Link> : <div key={t.id}>{inner}</div>;
          })}
        </aside>

        <div>
          {!owned && (
            <div className="card pad-lg mb" style={{ borderColor: "var(--brand)", borderWidth: 2 }}>
              <div className="flex between center-y wrap gap">
                <div>
                  <h3 style={{ margin: 0 }}>🔒 Enroll to unlock the full course</h3>
                  <p className="muted" style={{ margin: "4px 0 0" }}>The course guide below is free to preview. Lessons, practice, quizzes and tests need enrollment.</p>
                </div>
                <Link href={enrollHref} className="btn lg">Get access</Link>
              </div>
            </div>
          )}

          <h2>What this course covers</h2>
          <p>{course.tagline}</p>
          <div className="callout">
            <strong>About the exam.</strong> {course.examFacts.passNote}
          </div>

          <h3 className="mt-lg">The {stats.sections} knowledge areas</h3>
          <div className="grid cols-2 mt">
            {course.sections.map((s) => (
              <div key={s.id} className="card">
                <div className="flex between center-y">
                  <h4 style={{ margin: 0 }}>{s.title}</h4>
                  <span className="tag">{s.weight}</span>
                </div>
                <p className="muted" style={{ fontSize: 14, margin: "6px 0 10px" }}>{s.guide.overview.slice(0, 130)}…</p>
                {owned
                  ? <Link href={`/course/${courseId}/section/${s.id}`} className="btn secondary">Open</Link>
                  : <span className="tag">🔒 Enroll to open</span>}
              </div>
            ))}
          </div>

          <h3 className="mt-lg">Each section includes</h3>
          <div className="grid cols-4 mt">
            <div className="card feature"><div className="ic">📘</div><strong>Lesson</strong><p className="muted" style={{ fontSize: 13 }}>Concept teaching + key equations.</p></div>
            <div className="card feature"><div className="ic">✏️</div><strong>Practice</strong><p className="muted" style={{ fontSize: 13 }}>Worked, self-checking problems.</p></div>
            <div className="card feature"><div className="ic">🧪</div><strong>Quiz</strong><p className="muted" style={{ fontSize: 13 }}>Check your understanding.</p></div>
            <div className="card feature"><div className="ic">💡</div><strong>Learn &amp; Help</strong><p className="muted" style={{ fontSize: 13 }}>Step-by-step when you&apos;re stuck.</p></div>
          </div>
        </div>
      </div>
    </main>
  );
}
