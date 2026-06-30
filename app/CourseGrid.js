"use client";
import Link from "next/link";
import { useAuth } from "./AuthProvider";

export default function CourseGrid({ courses }) {
  const { user, hasCourse, ready } = useAuth();
  return (
    <div className="grid cols-3">
      {courses.map((c) => {
        const available = c.status === "available";
        const owned = ready && user && available && hasCourse(c.id);
        const href = available ? `/course/${c.id}` : "#";
        const Wrapper = available ? Link : "div";
        return (
          <Wrapper key={c.id} href={href} className="card course-card" style={{ opacity: available ? 1 : 0.75 }}>
            <div className="bar" style={{ background: c.color }} />
            <div className="flex between center-y">
              <h3 style={{ margin: 0 }}>{c.title}</h3>
              {owned ? <span className="badge owned">Enrolled</span>
                : available ? <span className="badge live">Available</span>
                : <span className="badge soon">Coming soon</span>}
            </div>
            <p className="muted" style={{ margin: 0 }}>{c.blurb}</p>
            {available && (
              <div style={{ marginTop: "auto", paddingTop: 10, fontWeight: 650, color: c.color }}>
                {owned ? "Continue →" : "View course →"}
              </div>
            )}
          </Wrapper>
        );
      })}
    </div>
  );
}
