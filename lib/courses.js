import catalog from "@/data/catalog.json";
import feMechanical from "@/data/course-fe-mechanical.json";

const COURSES = {
  "fe-mechanical": feMechanical,
};

export function getCatalog() { return catalog.courses; }
export function getCourse(id) { return COURSES[id] || null; }
export function getSection(courseId, sectionId) {
  const c = getCourse(courseId);
  if (!c) return null;
  return c.sections.find((s) => s.id === sectionId) || null;
}
export function getTest(courseId, testId) {
  const c = getCourse(courseId);
  if (!c) return null;
  return c.practiceTests.find((t) => t.id === testId) || null;
}
export function courseStats(courseId) {
  const c = getCourse(courseId);
  if (!c) return null;
  const problems = c.sections.reduce((n, s) => n + s.practiceProblems.length, 0);
  const quizQs = c.sections.reduce((n, s) => n + s.quiz.length, 0);
  const testQs = c.practiceTests.reduce((n, t) => n + t.questions.length, 0);
  return {
    sections: c.sections.length,
    problems, quizQs, testQs,
    totalQuestions: problems + quizQs + testQs,
    tests: c.practiceTests.length,
  };
}
