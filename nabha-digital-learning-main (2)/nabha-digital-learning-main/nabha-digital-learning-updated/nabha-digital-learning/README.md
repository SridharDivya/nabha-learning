# Digital Learning Platform for Rural School Students in Nabha

A Flask web app that lets teachers publish courses (text/video/PDF lessons + quizzes)
and lets students learn and take quizzes even with unreliable internet, since visited
pages are cached and quiz answers taken offline are queued and auto-submitted once
the connection returns.

## 1. Setup

```bash
cd nabha-digital-learning
python3 -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

Demo accounts (auto-created the first time you run the app):
- Teacher: `teacher@nabha.edu` / `teacher123`
- Student: `student@nabha.edu` / `student123`

## 2. Project Structure

```
nabha-digital-learning/
├── app.py                  # Flask routes (all backend logic)
├── models.py                # Database tables (SQLAlchemy models)
├── requirements.txt
├── instance/
│   └── app.db                # SQLite database (created automatically)
├── static/
│   ├── css/style.css         # All styling
│   ├── js/offline-sync.js    # Offline queue + sync logic
│   ├── service-worker.js     # Caches pages for offline use
│   ├── manifest.json         # Makes the site installable (PWA)
│   └── uploads/              # Place PDF lesson files here
└── templates/                # HTML pages (Jinja2)
    ├── base.html              # Shared layout (navbar, offline banner)
    ├── index.html, login.html, register.html
    ├── student_dashboard.html, teacher_dashboard.html
    ├── course.html, lesson.html
    ├── quiz.html, quiz_result.html
    ├── add_course.html, add_lesson.html, add_quiz.html, add_question.html
    └── teacher_students.html
```

## 3. How It Works

**Authentication** — `models.py` has one `User` table with a `role` column
(`student`/`teacher`). Passwords are hashed with Werkzeug's
`generate_password_hash`/`check_password_hash`, never stored in plain text.
`app.py` uses Flask `session` to remember who is logged in, and a
`login_required(role=...)` decorator to protect routes.

**Courses → Lessons → Quizzes** — A `Course` belongs to a `Course.class_grade`
(so students only see courses matching their own grade). Each course has
`Lesson`s (text, video embed, or PDF) and `Quiz`zes made of `Question`s with
4 options and one correct answer.

**Progress tracking** — Every time a student finishes a lesson, a row is
written to the `Progress` table. The student dashboard computes
`completed lessons / total lessons` per course to show a progress bar.
Every quiz submission is stored in `QuizAttempt` with a score, so the
teacher's "Students" page can see every attempt from every student.

**Offline support (the key feature for Nabha's connectivity problem)**
1. `service-worker.js` caches the CSS/JS app shell on first load, and then
   caches every lesson page as the student visits it (`cache-as-you-go`).
   If a page request fails (no network), the cached copy is served instead.
2. When a student submits a quiz, `quiz.html`'s JS checks
   `navigator.onLine`. If online, it submits normally. If offline, the
   answers are saved into `localStorage` via `queueOfflineSync.js`
   (`queueOfflineQuizAttempt`) instead of being lost.
3. `offline-sync.js` listens for the browser's `online` event. As soon as
   connectivity returns, it POSTs the whole local queue to `/api/sync`,
   which grades the quizzes and records lesson completions on the server,
   then clears the local queue.

This means a student can study a full lesson and take a quiz on a bus with
no signal, and everything is safely uploaded once they reach a school or
home with WiFi.

**Teacher dashboard** — Teachers create courses, add lessons/quizzes/questions
through simple forms, and can see every quiz attempt (including which ones
were `synced_offline`) plus a full student list on `/teacher/students`.

## 4. Ideas to Extend (for your report / viva)
- Add file upload for PDFs instead of typing a filename.
- Add SMS/IVR fallback for students with no smartphone (common ask for the
  real Nabha problem statement).
- Add multi-language support (Punjabi/Hindi/English) using Flask-Babel.
- Add a "download course for offline" button that pre-caches an entire
  course's lessons in one tap instead of relying only on pages already visited.
- Deploy with Gunicorn + Nginx, and switch SQLite to PostgreSQL for
  production scale.
