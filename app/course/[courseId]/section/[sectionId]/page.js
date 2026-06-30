"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../../../../AuthProvider";
import { getCourse, getSection } from "@/lib/courses";
import { Question } from "../../../../Question";

const TABS = ["Lesson", "Practice", "Quiz", "Learn & Help"];

export default function SectionPage({ params }) {
  const { courseId, sectionId } = params;
  const { user, ready, hasCourse, getProgress, markDone } = useAuth();
  const router = useRouter();
  const course = getCourse(courseId);
  const section = getSection(courseId, sectionId);
  const [tab, setTab] = useState("Lesson");
  const [done, setDone] = useState(false);

  const owned = ready && user && hasCourse(courseId);

  useEffect(() => {
    if (ready && !user) router.replace(`/login?next=${encodeURIComponent(`/course/${courseId}/section/${sectionId}`)}`);
  }, [ready, user, router, courseId, sectionId]);

  useEffect(() => {
    if (owned) setDone(!!getProgress(courseId)[sectionId]);
  }, [owned, courseId, sectionId, getProgress]);

  if (!course || !section) return <main className="container section">Section not found.</main>;
  if (!ready) return <main className="container section">Loading…</main>;

  if (user && !owned) {
    return (
      <main className="container section narrow center paywall">
        <div className="lock">🔒</div>
        <h1>This section is locked</h1>
        <p className="muted">Enroll in {course.title} to access lessons, practice, quizzes, and tests.</p>
        <div className="hero-cta" style={{ justifyContent: "center" }}>
          <Link href={`/checkout?course=${courseId}&plan=onetime`} className="btn lg">Enroll — $100 lifetime</Link>
          <Link href={`/checkout?course=${courseId}&plan=monthly`} className="btn lg secondary">$10/month</Link>
        </div>
      </main>
    );
  }
  if (!user) return <main className="container section">Loading…</main>;

  const idx = course.sections.findIndex((s) => s.id === sectionId);
  const prev = course.sections[idx - 1];
  const next = course.sections[idx + 1];
  const prog = getProgress(courseId);

  return (
    <div className="container course-shell">
      <aside className="sidebar">
        <Link href={`/course/${courseId}`} className="btn ghost" style={{ paddingLeft: 0 }}>← Course home</Link>
        <div className="sb-title">Knowledge areas</div>
        {course.sections.map((s) => (
          <Link key={s.id} href={`/course/${courseId}/section/${s.id}`}>
            <div className={`sb-item ${s.id === sectionId ? "active" : ""} ${prog[s.id] ? "done" : ""}`}>
              <span><span className="dot" /> {s.title}</span>
            </div>
          </Link>
        ))}
        <div className="sb-title mt">Practice tests</div>
        {course.practiceTests.map((t) => (
          <Link key={t.id} href={`/course/${courseId}/test/${t.id}`}>
            <div className="sb-item"><span>📝 {t.title.replace(/Practice Test \d+ - /, "")}</span></div>
          </Link>
        ))}
      </aside>

      <main>
        <div className="flex between center-y wrap gap">
          <div>
            <div className="muted" style={{ fontSize: 13, fontWeight: 700, letterSpacing: ".06em", textTransform: "uppercase" }}>Section {idx + 1} of {course.sections.length} · {section.weight} of exam</div>
            <h1 style={{ margin: "4px 0" }}>{section.title}</h1>
          </div>
          <span className="tag">Priority: {section.priority}</span>
        </div>

        <div className="tabs mt">
          {TABS.map((t) => (
            <div key={t} className={`tab ${tab === t ? "active" : ""}`} onClick={() => setTab(t)}>{t}</div>
          ))}
        </div>

        {tab === "Lesson" && (
          <div>
            <p style={{ fontSize: 17 }}>{section.guide.overview}</p>

            <h3 className="mt-lg">Learning objectives</h3>
            <ul>{section.guide.objectives.map((o, i) => <li key={i}>{o}</li>)}</ul>
            <p className="muted"><strong>Prerequisites:</strong> {section.guide.prereqs}</p>

            <h3 className="mt-lg">Key equations</h3>
            <table className="eq-table">
              <tbody>
                {section.keyEquations.map((e, i) => (
                  <tr key={i}><td className="name">{e.name}</td><td className="formula">{e.formula}</td><td className="where">{e.where}</td></tr>
                ))}
              </tbody>
            </table>

            <h3 className="mt-lg">The concepts</h3>
            {section.lesson.map((b, i) => (
              <div key={i} className="lesson-block"><h4>{b.heading}</h4><p>{b.body}</p></div>
            ))}

            <div className="callout warn">
              <strong>⚠ Watch out</strong>
              <ul style={{ margin: "6px 0 0" }}>{section.guide.watchOuts.map((w, i) => <li key={i}>{w}</li>)}</ul>
            </div>

            <div className="flex between center-y mt-lg wrap gap">
              <button className="btn secondary" onClick={() => setTab("Practice")}>Try practice problems →</button>
            </div>
          </div>
        )}

        {tab === "Practice" && (
          <div>
            <p className="muted">Pick an answer to instantly see whether you got it right, plus a worked solution.</p>
            {section.practiceProblems.map((q, i) => <Question key={q.id} q={q} index={i + 1} />)}
            <button className="btn secondary" onClick={() => setTab("Quiz")}>Take the quiz →</button>
          </div>
        )}

        {tab === "Quiz" && (
          <div>
            <p className="muted">A quick check of the essentials for {section.title}.</p>
            {section.quiz.map((q, i) => <Question key={q.id} q={q} index={i + 1} />)}
          </div>
        )}

        {tab === "Learn & Help" && (
          <div>
            <p className="muted">Stuck on a problem type? Here is every key equation and a fully worked solution for each practice problem in this section.</p>
            <h3>Formula sheet</h3>
            <table className="eq-table">
              <tbody>{section.keyEquations.map((e, i) => (
                <tr key={i}><td className="name">{e.name}</td><td className="formula">{e.formula}</td><td className="where">{e.where}</td></tr>
              ))}</tbody>
            </table>
            <h3 className="mt-lg">Worked solutions</h3>
            {section.practiceProblems.map((q, i) => (
              <div key={q.id} className="q-card">
                <div className="q-prompt">{i + 1}. {q.prompt}</div>
                <div style={{ fontWeight: 650, color: "var(--good)" }}>Answer: {["A", "B", "C", "D"][q.answer]}. {q.choices[q.answer]}</div>
                <div className="explain"><span className="lbl">How to solve it</span>{q.explanation}</div>
              </div>
            ))}
          </div>
        )}

        <div className="card mt-lg flex between center-y wrap gap">
          <div>
            <strong>{done ? "✅ Section marked complete" : "Finished this section?"}</strong>
            <div className="muted" style={{ fontSize: 14 }}>Mark it done to track your progress.</div>
          </div>
          <button className="btn" disabled={done} onClick={() => { markDone(courseId, sectionId); setDone(true); }}>
            {done ? "Completed" : "Mark complete"}
          </button>
        </div>

        <div className="flex between mt-lg">
          {prev ? <Link href={`/course/${courseId}/section/${prev.id}`} className="btn secondary">← {prev.title}</Link> : <span />}
          {next ? <Link href={`/course/${courseId}/section/${next.id}`} className="btn">{next.title} →</Link>
                : <Link href={`/course/${courseId}/test/${course.practiceTests[0].id}`} className="btn">Take a practice test →</Link>}
        </div>
      </main>
    </div>
  );
}
