import Link from "next/link";
import CourseGrid from "./CourseGrid";
import { getCatalog, courseStats } from "@/lib/courses";

export default function Home() {
  const courses = getCatalog();
  const s = courseStats("fe-mechanical");
  return (
    <main>
      <section className="hero">
        <div className="container">
          <div className="eyebrow">Engineering exam prep, done right</div>
          <h1>Stop guessing what to study. Start passing.</h1>
          <p className="lead">
            HallTestPrep turns the overwhelming FE syllabus into a clear path: structured lessons,
            worked practice problems, quizzes, and full-length practice tests — with a Learn &amp; Help
            explainer whenever you get stuck.
          </p>
          <div className="hero-cta">
            <Link href="/signup" className="btn lg">Start learning today</Link>
            <Link href="/course/fe-mechanical" className="btn lg secondary">Explore FE Mechanical</Link>
          </div>
          <div className="hero-stats">
            <div className="stat"><div className="n">{s.sections}</div><div className="l">Knowledge areas</div></div>
            <div className="stat"><div className="n">{s.totalQuestions}+</div><div className="l">Practice questions</div></div>
            <div className="stat"><div className="n">{s.tests}</div><div className="l">Full practice tests</div></div>
            <div className="stat"><div className="n">$10<span style={{fontSize:16}}>/mo</span></div><div className="l">or $100 lifetime</div></div>
          </div>
        </div>
      </section>

      <section className="section" id="courses">
        <div className="container">
          <div className="center mb">
            <h2>Pick your exam</h2>
            <p className="muted">FE Mechanical is live now. More courses are on the way.</p>
          </div>
          <CourseGrid courses={courses} />
        </div>
      </section>

      <section className="section tight">
        <div className="container">
          <div className="center mb"><h2>Everything in one place</h2></div>
          <div className="grid cols-4">
            <div className="card feature"><div className="ic">📘</div><h4>Guided lessons</h4><p className="muted">Plain-English teaching for every knowledge area, with the equations that actually show up.</p></div>
            <div className="card feature"><div className="ic">✏️</div><h4>Practice problems</h4><p className="muted">Exam-style multiple choice with fully worked solutions you can learn from.</p></div>
            <div className="card feature"><div className="ic">🧪</div><h4>Quizzes &amp; tests</h4><p className="muted">Section quizzes and timed, mixed practice tests that mirror the real CBT.</p></div>
            <div className="card feature"><div className="ic">💡</div><h4>Learn &amp; Help</h4><p className="muted">Stuck on a problem? Every question has a step-by-step explanation on demand.</p></div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container narrow center">
          <h2>Simple pricing</h2>
          <p className="muted">Per course. $10/month, or pay $100 once for lifetime access to that course.</p>
          <Link href="/pricing" className="btn lg mt">See pricing</Link>
        </div>
      </section>
    </main>
  );
}
