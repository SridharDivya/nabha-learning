# Nabha Digital Learning

A Flask platform for rural school students (Classes 5-10) in Nabha, Punjab.

- Students choose their class at registration and see only that class's subjects, lessons, quizzes, timetable and attendance.
- Teachers manage Classes 5-10 from the Teacher Dashboard: subjects, lessons, quizzes, timetable, attendance.
- AI assistant for students (tutor) and teachers (lesson plans, quiz questions).

## Run locally
```
pip install -r requirements.txt
python app.py
```

## Render settings
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Environment variables:
  - `PYTHON_VERSION` = `3.12.3`
  - `SECRET_KEY` = any long random text
  - `GEMINI_API_KEY` = (optional, free) key from aistudio.google.com/app/apikey; enables full AI answers
  - `GEMINI_MODEL` = (optional) defaults to `gemini-3.8-flash`
  - `ANTHROPIC_API_KEY` = (optional, paid) alternative provider; `AI_MODEL` sets its model
  - without any key the assistant searches the lessons
  - `TEACHER_CODE` = (optional) if set, teachers must enter this code to register
  - `DATABASE_URL` = (optional) PostgreSQL URL to keep data between deploys
