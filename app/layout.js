import "./globals.css";
import { AuthProvider } from "./AuthProvider";
import Nav from "./Nav";

export const metadata = {
  title: "HallTestPrep — Pass the FE the smart way",
  description: "Structured lessons, worked practice problems, quizzes, and full practice tests for the FE Mechanical exam and more.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <Nav />
          {children}
          <footer className="footer">
            <div className="container flex between wrap gap">
              <div>
                <div className="brand" style={{ color: "#fff", marginBottom: 8 }}>
                  <span className="mark"><small>H</small></span> HallTestPrep
                </div>
                <div>Pass your engineering exams with a plan, not a pile of PDFs.</div>
              </div>
              <div style={{ maxWidth: 360 }}>
                © {new Date().getFullYear()} HallTestPrep. Not affiliated with or endorsed by NCEES.
                FE® is a registered trademark of NCEES.
              </div>
            </div>
          </footer>
        </AuthProvider>
      </body>
    </html>
  );
}
