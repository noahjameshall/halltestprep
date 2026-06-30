"use client";
import { createContext, useContext, useEffect, useState, useCallback } from "react";

const AuthCtx = createContext(null);
const LS_USERS = "htp_users";
const LS_SESSION = "htp_session";

function load(key, fallback) {
  if (typeof window === "undefined") return fallback;
  try { return JSON.parse(localStorage.getItem(key)) ?? fallback; }
  catch { return fallback; }
}
function save(key, val) {
  if (typeof window !== "undefined") localStorage.setItem(key, JSON.stringify(val));
}

export function AuthProvider({ children }) {
  const [ready, setReady] = useState(false);
  const [user, setUser] = useState(null); // {email, name}
  const [db, setDb] = useState({}); // email -> {password,name,entitlements:{},progress:{}}

  useEffect(() => {
    const users = load(LS_USERS, {});
    const session = load(LS_SESSION, null);
    setDb(users);
    if (session && users[session]) setUser({ email: session, name: users[session].name });
    setReady(true);
  }, []);

  const persist = useCallback((nextDb) => { setDb(nextDb); save(LS_USERS, nextDb); }, []);

  const signup = useCallback((email, password, name) => {
    email = email.trim().toLowerCase();
    const users = load(LS_USERS, {});
    if (users[email]) return { ok: false, error: "An account with that email already exists. Try logging in." };
    users[email] = { password, name: name || email.split("@")[0], entitlements: {}, progress: {} };
    save(LS_USERS, users); setDb(users);
    save(LS_SESSION, email); setUser({ email, name: users[email].name });
    return { ok: true };
  }, []);

  const login = useCallback((email, password) => {
    email = email.trim().toLowerCase();
    const users = load(LS_USERS, {});
    if (!users[email]) return { ok: false, error: "No account found for that email. Sign up first." };
    if (users[email].password !== password) return { ok: false, error: "Incorrect password." };
    save(LS_SESSION, email); setUser({ email, name: users[email].name });
    return { ok: true };
  }, []);

  const logout = useCallback(() => { save(LS_SESSION, null); setUser(null); }, []);

  const hasCourse = useCallback((courseId) => {
    if (!user) return false;
    const users = load(LS_USERS, {});
    const e = users[user.email]?.entitlements?.[courseId];
    return !!e && (e.type === "onetime" || e.type === "subscription");
  }, [user]);

  const grantCourse = useCallback((courseId, type) => {
    if (!user) return;
    const users = load(LS_USERS, {});
    if (!users[user.email]) return;
    users[user.email].entitlements = users[user.email].entitlements || {};
    users[user.email].entitlements[courseId] = { type, since: Date.now() };
    persist(users);
  }, [user, persist]);

  const getProgress = useCallback((courseId) => {
    if (!user) return {};
    const users = load(LS_USERS, {});
    return users[user.email]?.progress?.[courseId] || {};
  }, [user]);

  const markDone = useCallback((courseId, sectionId) => {
    if (!user) return;
    const users = load(LS_USERS, {});
    const u = users[user.email];
    if (!u) return;
    u.progress = u.progress || {};
    u.progress[courseId] = u.progress[courseId] || {};
    u.progress[courseId][sectionId] = true;
    persist(users);
  }, [user, persist]);

  const value = { ready, user, signup, login, logout, hasCourse, grantCourse, getProgress, markDone, db };
  return <AuthCtx.Provider value={value}>{children}</AuthCtx.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthCtx);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}
