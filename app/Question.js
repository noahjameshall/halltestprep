"use client";
import { useState } from "react";

const LETTERS = ["A", "B", "C", "D", "E", "F"];

// Single self-checking question (used in Practice + Quiz).
export function Question({ q, index }) {
  const [picked, setPicked] = useState(null);
  const [revealed, setRevealed] = useState(false);

  function choose(i) {
    if (revealed) return;
    setPicked(i);
    setRevealed(true);
  }

  return (
    <div className="q-card">
      <div className="q-prompt">{index != null ? `${index}. ` : ""}{q.prompt}</div>
      {q.choices.map((c, i) => {
        let cls = "choice";
        if (revealed) {
          if (i === q.answer) cls += " correct";
          else if (i === picked) cls += " wrong";
        } else if (i === picked) cls += " selected";
        return (
          <div key={i} className={cls} onClick={() => choose(i)}>
            <span className="key">{LETTERS[i]}</span>
            <span>{c}</span>
          </div>
        );
      })}
      {revealed && (
        <div className="explain">
          <span className="lbl">{picked === q.answer ? "✓ Correct" : "✗ Not quite"} — Learn &amp; Help</span>
          {q.explanation}
        </div>
      )}
    </div>
  );
}

// Timed/graded test runner.
export function TestRunner({ test }) {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const total = test.questions.length;
  const answeredCount = Object.keys(answers).length;
  const score = test.questions.reduce((n, q) => n + (answers[q.id] === q.answer ? 1 : 0), 0);
  const pct = Math.round((score / total) * 100);

  return (
    <div>
      {submitted && (
        <div className="card pad-lg mb" style={{ textAlign: "center" }}>
          <div className="score-ring" style={{ color: pct >= 70 ? "var(--good)" : pct >= 50 ? "var(--accent)" : "var(--bad)" }}>{pct}%</div>
          <p style={{ margin: 0 }}>You scored <strong>{score} / {total}</strong>.</p>
          <p className="muted" style={{ fontSize: 14 }}>
            {pct >= 60 ? "That's around the FE passing range — keep it up." : "Below the typical FE cut score. Review the explanations and retry."}
          </p>
          <button className="btn secondary mt" onClick={() => { setAnswers({}); setSubmitted(false); window.scrollTo(0, 0); }}>Retake test</button>
        </div>
      )}

      {test.questions.map((q, idx) => {
        const picked = answers[q.id];
        return (
          <div key={q.id} className="q-card">
            <div className="q-prompt">{idx + 1}. {q.prompt}</div>
            {q.choices.map((c, i) => {
              let cls = "choice";
              if (submitted) {
                if (i === q.answer) cls += " correct";
                else if (i === picked) cls += " wrong";
              } else if (i === picked) cls += " selected";
              return (
                <div key={i} className={cls} onClick={() => !submitted && setAnswers((a) => ({ ...a, [q.id]: i }))}>
                  <span className="key">{["A", "B", "C", "D", "E"][i]}</span>
                  <span>{c}</span>
                </div>
              );
            })}
            {submitted && (
              <div className="explain"><span className="lbl">Explanation</span>{q.explanation}</div>
            )}
          </div>
        );
      })}

      {!submitted && (
        <div className="flex between center-y wrap gap mt">
          <span className="muted">{answeredCount} of {total} answered</span>
          <button className="btn lg" onClick={() => { setSubmitted(true); window.scrollTo(0, 0); }}>Submit test</button>
        </div>
      )}
    </div>
  );
}
