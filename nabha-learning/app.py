import os
import re
from datetime import datetime, timedelta, date
from functools import wraps

from flask import (Flask, render_template, request, redirect, url_for, flash,
                   session, abort, jsonify)
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import inspect, text

from models import (db, User, Subject, Unit, Quiz, Question, QuizResult,
                    TimetableEntry, Attendance)
from curriculum_data import CURRICULUM
from ai_assistant import ask_ai, ai_enabled

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'nabha-digital-secret-key-2026')

# Database URI configuration for Render (PostgreSQL) supporting psycopg v3
database_url = os.environ.get('DATABASE_URL', 'sqlite:///nabha.db')
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

GRADES = sorted(CURRICULUM)                      # [5, 6, 7, 8, 9, 10]
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
DEFAULT_PERIODS = [(1, '09:00', '09:45'), (2, '09:45', '10:30'), (3, '10:30', '11:15'),
                   (4, '11:30', '12:15'), (5, '12:15', '13:00'), (6, '13:00', '13:45')]


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ----------------------------------------------------------------- helpers
def now_ist():
    return datetime.utcnow() + timedelta(hours=5, minutes=30)


def grade_label(grade):
    return f'Class {grade}'


def teacher_required(view):
    @wraps(view)
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.role != 'teacher':
            flash('Teacher access required.', 'danger')
            return redirect(url_for('index'))
        return view(*args, **kwargs)
    return wrapper


def student_required(view):
    @wraps(view)
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.role != 'student':
            return redirect(url_for('teacher_dashboard'))
        if not current_user.grade:
            return redirect(url_for('set_class'))
        return view(*args, **kwargs)
    return wrapper


def can_access_subject(subject):
    if current_user.role == 'teacher':
        return True
    return bool(current_user.grade) and subject.grade_level == grade_label(current_user.grade)


def class_subjects(grade):
    return Subject.query.filter_by(grade_level=grade_label(grade)).order_by(Subject.id).all()


def attendance_stats(user_id):
    records = Attendance.query.filter_by(user_id=user_id).all()
    total = len(records)
    present = sum(1 for r in records if r.status == 'present')
    pct = round(present * 100 / total) if total else None
    return {'present': present, 'total': total, 'pct': pct}


def build_timetable(grade):
    entries = TimetableEntry.query.filter_by(grade=grade).all()
    times = {}
    for e in sorted(entries, key=lambda x: (x.period, x.start_time)):
        times.setdefault(e.period, (e.start_time, e.end_time))
    periods = [{'number': n, 'start': t[0], 'end': t[1]} for n, t in sorted(times.items())]
    grid = {(e.period, e.day): e for e in entries}
    return periods, grid


def youtube_embed(url):
    if not url:
        return None
    match = re.search(r'(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|shorts/))([\w-]{11})', url)
    return f'https://www.youtube.com/embed/{match.group(1)}' if match else None


app.jinja_env.filters['youtube_embed'] = youtube_embed


# ------------------------------------------------- database set-up / seed
def ensure_columns():
    """Add columns introduced after the first release (create_all doesn't alter tables)."""
    inspector = inspect(db.engine)
    if 'grade' not in {c['name'] for c in inspector.get_columns('users')}:
        db.session.execute(text('ALTER TABLE users ADD COLUMN grade INTEGER'))
    if 'video_url' not in {c['name'] for c in inspector.get_columns('units')}:
        db.session.execute(text('ALTER TABLE units ADD COLUMN video_url VARCHAR(300)'))
    db.session.commit()


def seed_curriculum():
    """Add the starter Class 5-10 subjects and units. Safe to run repeatedly:
    a subject that already exists for a class is left untouched."""
    for grade, subjects in CURRICULUM.items():
        for title, description, units in subjects:
            if Subject.query.filter_by(title=title, grade_level=grade_label(grade)).first():
                continue
            subject = Subject(title=title, description=description, grade_level=grade_label(grade))
            for number, (unit_title, content) in enumerate(units, start=1):
                subject.units.append(Unit(unit_number=number, title=unit_title, content=content))
            db.session.add(subject)
    db.session.commit()


def seed_timetable():
    """Give every class a starter Monday-Saturday timetable (teachers can edit it)."""
    for grade, subjects in CURRICULUM.items():
        if TimetableEntry.query.filter_by(grade=grade).first():
            continue
        names = [s[0] for s in subjects]
        for day in range(len(DAYS)):
            for number, start, end in DEFAULT_PERIODS:
                db.session.add(TimetableEntry(
                    grade=grade, day=day, period=number,
                    subject_name=names[(day + number - 1) % len(names)],
                    start_time=start, end_time=end))
    db.session.commit()


with app.app_context():
    db.create_all()
    ensure_columns()
    seed_curriculum()
    seed_timetable()


@app.context_processor
def inject_globals():
    languages = {'en': 'English', 'hi': 'Hindi', 'te': 'Telugu', 'es': 'Spanish', 'fr': 'French'}
    return dict(supported_languages=languages, grades=GRADES, days=DAYS)


# ------------------------------------------------------------- public pages
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set_language', methods=['POST'])
def set_language():
    session['language'] = request.form.get('language', 'en')
    return redirect(request.referrer or url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = (request.form.get('username') or request.form.get('email') or '').strip()
        password = request.form.get('password') or ''
        user = User.query.filter((User.username == login_input) | (User.email == login_input)).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('teacher_dashboard' if user.role == 'teacher' else 'student_dashboard'))
        flash('Invalid username/email or password', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    teacher_code = os.environ.get('TEACHER_CODE')
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        email = (request.form.get('email') or '').strip().lower()
        password = request.form.get('password') or ''
        role = request.form.get('role', 'student')
        grade = request.form.get('grade', type=int)

        def fail(message):
            flash(message, 'danger')
            return render_template('register.html', teacher_code_required=bool(teacher_code), form=request.form)

        if not username or not email or len(password) < 6:
            return fail('Please fill every field. Password needs at least 6 characters.')
        if role not in ('student', 'teacher'):
            role = 'student'
        if role == 'student' and grade not in GRADES:
            return fail('Please choose your class (5 to 10).')
        if role == 'teacher' and teacher_code and request.form.get('teacher_code') != teacher_code:
            return fail('Wrong teacher access code.')
        if User.query.filter_by(username=username).first():
            return fail('Username already exists.')
        if User.query.filter_by(email=email).first():
            return fail('An account with this email already exists.')

        db.session.add(User(username=username, email=email,
                            password_hash=generate_password_hash(password),
                            role=role, grade=grade if role == 'student' else None))
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', teacher_code_required=bool(teacher_code), form={})


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# ----------------------------------------------------------------- student
@app.route('/student/set-class', methods=['GET', 'POST'])
@login_required
def set_class():
    if current_user.role != 'student':
        return redirect(url_for('teacher_dashboard'))
    if request.method == 'POST':
        grade = request.form.get('grade', type=int)
        if grade in GRADES:
            current_user.grade = grade
            db.session.commit()
            return redirect(url_for('student_dashboard'))
        flash('Please choose a class between 5 and 10.', 'danger')
    return render_template('set_class.html')


@app.route('/student/dashboard')
@student_required
def student_dashboard():
    grade = current_user.grade
    subjects = class_subjects(grade)
    results = QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.completed_at.desc()).all()
    avg_score = round(sum(r.score for r in results) / len(results)) if results else 0

    today = now_ist()
    today_classes = []
    if today.weekday() < len(DAYS):
        today_classes = (TimetableEntry.query.filter_by(grade=grade, day=today.weekday())
                         .order_by(TimetableEntry.period).all())
    quizzes_available = sum(len(u.quizzes) for s in subjects for u in s.units)

    return render_template('student_dashboard.html', subjects=subjects, results=results[:5],
                           total_quizzes=len(results), avg_score=avg_score,
                           attendance=attendance_stats(current_user.id),
                           today_classes=today_classes, today_name=today.strftime('%A'),
                           quizzes_available=quizzes_available)


@app.route('/student/timetable')
@student_required
def student_timetable():
    periods, grid = build_timetable(current_user.grade)
    today = now_ist().weekday()
    return render_template('student_timetable.html', grade=current_user.grade, periods=periods,
                           grid=grid, today_idx=today, editable=False)


@app.route('/student/attendance')
@student_required
def student_attendance():
    records = (Attendance.query.filter_by(user_id=current_user.id)
               .order_by(Attendance.date.desc()).all())
    return render_template('student_attendance.html', records=records,
                           stats=attendance_stats(current_user.id))


# ------------------------------------------------ subjects, lessons, quizzes
@app.route('/subject/<int:subject_id>')
@login_required
def subject_detail(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    if not can_access_subject(subject):
        flash('That subject belongs to a different class.', 'danger')
        return redirect(url_for('student_dashboard'))
    units = sorted(subject.units, key=lambda u: u.unit_number)
    done = {}
    if current_user.role == 'student':
        for r in QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.completed_at):
            done[r.quiz_id] = r.score          # latest attempt wins
    return render_template('subject_detail.html', subject=subject, units=units, done=done)


@app.route('/quiz/<int:quiz_id>')
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if not can_access_subject(quiz.unit.subject):
        abort(403)
    if not quiz.questions:
        flash('This quiz has no questions yet.', 'danger')
        return redirect(url_for('subject_detail', subject_id=quiz.unit.subject_id))
    return render_template('quiz.html', quiz=quiz)


@app.route('/quiz/<int:quiz_id>/submit', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if not can_access_subject(quiz.unit.subject):
        abort(403)

    review, correct_count = [], 0
    for question in quiz.questions:
        selected = (request.form.get(f'question_{question.id}') or '').upper()
        is_right = selected == question.correct_option.upper()
        correct_count += is_right
        review.append({'question': question, 'selected': selected, 'right': is_right})

    total = len(quiz.questions)
    score_pct = round(correct_count * 100 / total) if total else 0

    if current_user.role == 'student':
        db.session.add(QuizResult(user_id=current_user.id, quiz_id=quiz.id,
                                  score=score_pct, total_questions=total))
        db.session.commit()
    return render_template('quiz_result.html', quiz=quiz, score=score_pct,
                           correct=correct_count, total=total, review=review)


# ----------------------------------------------------------------- teacher
@app.route('/teacher/dashboard')
@teacher_required
def teacher_dashboard():
    all_results = QuizResult.query.all()
    class_avg = round(sum(r.score for r in all_results) / len(all_results)) if all_results else 0
    cards = []
    for grade in GRADES:
        cards.append({
            'grade': grade,
            'subjects': class_subjects(grade),
            'students': User.query.filter_by(role='student', grade=grade).count(),
        })
    return render_template('teacher_dashboard.html', cards=cards,
                           total_students=User.query.filter_by(role='student').count(),
                           total_quizzes=Quiz.query.count(), class_avg=class_avg)


@app.route('/teacher/class/<int:grade>')
@teacher_required
def teacher_class(grade):
    if grade not in GRADES:
        abort(404)
    students = User.query.filter_by(role='student', grade=grade).order_by(User.username).all()
    rows = []
    for s in students:
        results = QuizResult.query.filter_by(user_id=s.id).all()
        rows.append({'student': s, 'attendance': attendance_stats(s.id),
                     'quizzes': len(results),
                     'avg': round(sum(r.score for r in results) / len(results)) if results else None})
    return render_template('teacher_class.html', grade=grade, subjects=class_subjects(grade), rows=rows)


@app.route('/teacher/class/<int:grade>/attendance', methods=['GET', 'POST'])
@teacher_required
def teacher_attendance(grade):
    if grade not in GRADES:
        abort(404)
    students = User.query.filter_by(role='student', grade=grade).order_by(User.username).all()
    raw_date = request.values.get('date') or now_ist().strftime('%Y-%m-%d')
    try:
        day = datetime.strptime(raw_date, '%Y-%m-%d').date()
    except ValueError:
        day = now_ist().date()

    if request.method == 'POST':
        if day > now_ist().date():
            flash('You cannot mark attendance for a future date.', 'danger')
        else:
            for s in students:
                status = 'present' if request.form.get(f'status_{s.id}') == 'present' else 'absent'
                record = Attendance.query.filter_by(user_id=s.id, date=day).first()
                if record:
                    record.status, record.marked_by = status, current_user.id
                else:
                    db.session.add(Attendance(user_id=s.id, date=day, status=status, marked_by=current_user.id))
            db.session.commit()
            flash(f'Attendance saved for {day.strftime("%d %b %Y")}.', 'success')
        return redirect(url_for('teacher_attendance', grade=grade, date=day.isoformat()))

    existing = {a.user_id: a.status for a in Attendance.query.filter_by(date=day)
                .filter(Attendance.user_id.in_([s.id for s in students] or [0])).all()}
    return render_template('teacher_attendance.html', grade=grade, students=students,
                           day=day, existing=existing, today=now_ist().date())


@app.route('/teacher/class/<int:grade>/timetable')
@teacher_required
def teacher_timetable(grade):
    if grade not in GRADES:
        abort(404)
    periods, grid = build_timetable(grade)
    return render_template('teacher_timetable.html', grade=grade, periods=periods, grid=grid,
                           today_idx=now_ist().weekday(), editable=True,
                           subject_names=[s.title for s in class_subjects(grade)],
                           defaults=DEFAULT_PERIODS)


@app.route('/teacher/class/<int:grade>/timetable/add', methods=['POST'])
@teacher_required
def add_timetable_entry(grade):
    if grade not in GRADES:
        abort(404)
    day = request.form.get('day', type=int)
    period = request.form.get('period', type=int)
    name = (request.form.get('subject_name') or '').strip()
    start, end = request.form.get('start_time', ''), request.form.get('end_time', '')
    time_ok = all(re.fullmatch(r'\d{2}:\d{2}', t) for t in (start, end))
    if day not in range(len(DAYS)) or not period or not name or not time_ok:
        flash('Please fill day, period, subject and both times.', 'danger')
    else:
        entry = TimetableEntry.query.filter_by(grade=grade, day=day, period=period).first()
        if entry:
            entry.subject_name, entry.start_time, entry.end_time = name, start, end
        else:
            db.session.add(TimetableEntry(grade=grade, day=day, period=period,
                                          subject_name=name, start_time=start, end_time=end))
        db.session.commit()
        flash('Timetable updated.', 'success')
    return redirect(url_for('teacher_timetable', grade=grade))


@app.route('/teacher/timetable/<int:entry_id>/delete', methods=['POST'])
@teacher_required
def delete_timetable_entry(entry_id):
    entry = TimetableEntry.query.get_or_404(entry_id)
    grade = entry.grade
    db.session.delete(entry)
    db.session.commit()
    flash('Timetable slot removed.', 'success')
    return redirect(url_for('teacher_timetable', grade=grade))


@app.route('/teacher/subject/add', methods=['POST'])
@teacher_required
def add_subject():
    title = (request.form.get('title') or '').strip()
    grade = request.form.get('grade', type=int)
    if not title or grade not in GRADES:
        flash('Subject title and a class (5-10) are required.', 'danger')
        return redirect(url_for('teacher_dashboard'))
    subject = Subject(title=title, grade_level=grade_label(grade),
                      description=(request.form.get('description') or '').strip() or None)
    db.session.add(subject)
    db.session.commit()
    flash(f'Subject "{title}" added to {grade_label(grade)}.', 'success')
    return redirect(url_for('teacher_subject', subject_id=subject.id))


@app.route('/teacher/subject/<int:subject_id>')
@teacher_required
def teacher_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    units = sorted(subject.units, key=lambda u: u.unit_number)
    grade = int(subject.grade_level.replace('Class ', '')) if subject.grade_level else None
    return render_template('teacher_subject.html', subject=subject, units=units, grade=grade)


@app.route('/teacher/subject/<int:subject_id>/delete', methods=['POST'])
@teacher_required
def delete_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    grade = subject.grade_level.replace('Class ', '')
    db.session.delete(subject)
    db.session.commit()
    flash('Subject deleted.', 'success')
    return redirect(url_for('teacher_class', grade=int(grade)) if grade.isdigit() else url_for('teacher_dashboard'))


def clean_video_url(value):
    value = (value or '').strip()
    return value if value.startswith(('http://', 'https://')) else None


@app.route('/teacher/subject/<int:subject_id>/unit/add', methods=['POST'])
@teacher_required
def add_unit(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    title = (request.form.get('title') or '').strip()
    if not title:
        flash('Lesson title is required.', 'danger')
    else:
        next_number = max([u.unit_number for u in subject.units] or [0]) + 1
        db.session.add(Unit(subject_id=subject.id, unit_number=next_number, title=title,
                            content=(request.form.get('content') or '').strip(),
                            video_url=clean_video_url(request.form.get('video_url'))))
        db.session.commit()
        flash('Lesson added. Students of this class can see it now.', 'success')
    return redirect(url_for('teacher_subject', subject_id=subject.id))


@app.route('/teacher/unit/<int:unit_id>/edit', methods=['GET', 'POST'])
@teacher_required
def edit_unit(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    if request.method == 'POST':
        title = (request.form.get('title') or '').strip()
        if not title:
            flash('Lesson title is required.', 'danger')
        else:
            unit.title = title
            unit.content = (request.form.get('content') or '').strip()
            unit.video_url = clean_video_url(request.form.get('video_url'))
            db.session.commit()
            flash('Lesson updated.', 'success')
            return redirect(url_for('teacher_subject', subject_id=unit.subject_id))
    return render_template('edit_unit.html', unit=unit)


@app.route('/teacher/unit/<int:unit_id>/delete', methods=['POST'])
@teacher_required
def delete_unit(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    subject_id = unit.subject_id
    db.session.delete(unit)
    db.session.commit()
    flash('Lesson deleted.', 'success')
    return redirect(url_for('teacher_subject', subject_id=subject_id))


@app.route('/teacher/unit/<int:unit_id>/quiz/add', methods=['POST'])
@teacher_required
def add_quiz(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    title = (request.form.get('title') or '').strip() or f'{unit.title} Quiz'
    quiz = Quiz(unit_id=unit.id, title=title)
    db.session.add(quiz)
    db.session.commit()
    flash('Quiz created. Now add its questions.', 'success')
    return redirect(url_for('teacher_quiz', quiz_id=quiz.id))


@app.route('/teacher/quiz/<int:quiz_id>')
@teacher_required
def teacher_quiz(quiz_id):
    return render_template('teacher_quiz.html', quiz=Quiz.query.get_or_404(quiz_id))


@app.route('/teacher/quiz/<int:quiz_id>/question/add', methods=['POST'])
@teacher_required
def add_question(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    f = request.form
    fields = [(f.get(k) or '').strip() for k in ('question_text', 'option_a', 'option_b', 'option_c', 'option_d')]
    correct = (f.get('correct_option') or '').upper()
    if not all(fields) or correct not in ('A', 'B', 'C', 'D'):
        flash('Fill the question, all four options and choose the correct one.', 'danger')
    else:
        db.session.add(Question(quiz_id=quiz.id, question_text=fields[0], option_a=fields[1],
                                option_b=fields[2], option_c=fields[3], option_d=fields[4],
                                correct_option=correct))
        db.session.commit()
        flash('Question added.', 'success')
    return redirect(url_for('teacher_quiz', quiz_id=quiz.id))


@app.route('/teacher/question/<int:question_id>/delete', methods=['POST'])
@teacher_required
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    quiz_id = question.quiz_id
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('teacher_quiz', quiz_id=quiz_id))


@app.route('/teacher/quiz/<int:quiz_id>/delete', methods=['POST'])
@teacher_required
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    subject_id = quiz.unit.subject_id
    QuizResult.query.filter_by(quiz_id=quiz.id).delete()
    db.session.delete(quiz)
    db.session.commit()
    flash('Quiz deleted.', 'success')
    return redirect(url_for('teacher_subject', subject_id=subject_id))


# ------------------------------------------------------------ AI assistant
@app.route('/assistant')
@login_required
def assistant():
    if current_user.role == 'student' and not current_user.grade:
        return redirect(url_for('set_class'))
    ai_on = ai_enabled()
    return render_template('assistant.html', ai_on=ai_on)


@app.route('/api/assistant', methods=['POST'])
@login_required
def assistant_api():
    data = request.get_json(silent=True) or {}
    if current_user.role == 'student':
        if not current_user.grade:
            return jsonify({'reply': 'Please choose your class first.', 'source': 'none'}), 400
        subjects = class_subjects(current_user.grade)
        units = Unit.query.join(Subject).filter(Subject.grade_level == grade_label(current_user.grade)).all()
    else:
        subjects = Subject.query.all()
        units = Unit.query.all()
    titles = sorted({s.title for s in subjects})
    result = ask_ai(current_user.role, current_user.grade, titles,
                    data.get('message'), data.get('history'), units)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
