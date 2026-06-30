"use client";
import { useEffect, Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useAuth } from "../../AuthProvider";
import { getCatalog } from "@/lib/courses";

function SuccessInner() {
  const { user, ready, grantCourse } = useAuth();
  const params = useSearchParams();
  const courseId = params.get("course") || "fe-mechanical";
  const plan = params.get("plan") || "onetime";
  const course = getCatalog().find((c) => c.id === courseId);

  useEffect(() => {
    if (ready && user) grantCourse(courseId, plan === "monthly" ? "subscription" : "onetime");
  }, [ready, user, courseId, plan, grantCourse]);

  return (
    <main className="container section narrow center">
      <div className="lock">🎉</div>
      <h1>You&apos;re in!</h1>
      <p className="muted">Payment received. You now have access to {course ? course.title : "your course"}.</p>
      <Link href={`/course/${courseId}`} className="btn lg mt">Start studying</Link>
    </main>
  );
}

export default function SuccessPage() {
  return <Suspense><SuccessInner /></Suspense>;
}
