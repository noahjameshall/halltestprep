"use client";
import { use, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../../../../AuthProvider";
import { getCourse, getTest } from "@/lib/courses";
import { TestRunner } from "../../../../Question";

export default function TestPage({ params }) {
  const { courseId, testId } = use(params);
  const { user, ready, hasCourse } = useAuth();
  const router = useRouter();
  const course = getCourse(courseId);
  const test = getTest(courseId, testId);
  const owned = ready && user && hasCourse(courseId);

  useEffect(() => {
    if (ready && !user) router.replace(`/login?next=${encodeURIComponent(`/course/${courseId}/test/${testId}`)}`);
  }, [ready, user, router, courseId, testId]);

  if (!course || !test) return <main className="container section">Test not found.</main>;
  if (!ready || !user) return <main className="container section">Loading…</main>;

  if (!owned) {
    return (
      <main className="container section narrow center paywall">
        <div className="lock">🔒</div>
        <h1>Practice tests are locked</h1>
        <p className="muted">Enroll in {course.title} to take full practice tests.</p>
        <Link href={`/checkout?course=${courseId}&plan=onetime`} className="btn lg mt">Enroll now</Link>
      </main>
    );
  }

  return (
    <main className="container section">
      <Link href={`/course/${courseId}`} className="btn ghost" style={{ paddingLeft: 0 }}>← Course home</Link>
      <h1 style={{ marginTop: 6 }}>{test.title}</h1>
      <p className="muted">{test.questions.length} questions · suggested time {test.time}. Answer all, then submit to see your score and explanations.</p>
      <div className="mt">
        <TestRunner test={test} />
      </div>
      <div className="mt-lg">
        {course.practiceTests.filter((t) => t.id !== testId).map((t) => (
          <Link key={t.id} href={`/course/${courseId}/test/${t.id}`} className="btn secondary" style={{ marginRight: 10 }}>Try: {t.title.replace(/Practice Test \d+ - /, "")} →</Link>
        ))}
      </div>
    </main>
  );
}
