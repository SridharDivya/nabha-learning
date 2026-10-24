import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Subject, Unit, Quiz, Question, QuizResult

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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize database tables safely within app context
with app.app_context():
    db.create_all()

@app.context_processor
def inject_languages():
    languages = {
        'en': 'English',
        'hi': 'Hindi',
        'te': 'Telugu',
        'es': 'Spanish',
        'fr': 'French'
    }
    return dict(supported_languages=languages)

@app.route('/')
def index():
    subjects = Subject.query.all()
    return render_template('index.html', subjects=subjects)

@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('language', 'en')
    session['language'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = request.form.get('username') or request.form.get('email')
        password = request.form.get('password')
        
        # Allow login using either username or email
        user = User.query.filter(
            (User.username == login_input) | (User.email == login_input)
        ).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            if user.role == 'teacher':
                return redirect(url_for('teacher_dashboard'))
            return redirect(url_for('student_dashboard'))
        flash('Invalid username/email or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'student')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
            
        hashed_pwd = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_pwd, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    subjects = Subject.query.all()
    results = QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.completed_at.desc()).all()
    
    total_quizzes = len(results)
    avg_score = (sum(r.score for r in results) / total_quizzes) if total_quizzes > 0 else 0
    
    return render_template(
        'student_dashboard.html', 
        subjects=subjects, 
        results=results, 
        total_quizzes=total_quizzes, 
        avg_score=round(avg_score, 1)
    )

@app.route('/teacher/dashboard')
@login_required
def teacher_dashboard():
    if current_user.role != 'teacher':
        flash('Teacher access required.', 'danger')
        return redirect(url_for('index'))
        
    subjects = Subject.query.all()
    total_students = User.query.filter_by(role='student').count()
    total_quizzes = Quiz.query.count()
    all_results = QuizResult.query.all()
    
    class_avg = (sum(r.score for r in all_results) / len(all_results)) if all_results else 0

    return render_template(
        'teacher_dashboard.html', 
        subjects=subjects, 
        total_students=total_students, 
        total_quizzes=total_quizzes, 
        class_avg=round(class_avg, 1)
    )

@app.route('/quiz/<int:quiz_id>')
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz.html', quiz=quiz)

@app.route('/quiz/<int:quiz_id>/submit', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    correct_count = 0
    
    for question in quiz.questions:
        selected = request.form.get(f'question_{question.id}')
        if selected and selected.upper() == question.correct_option.upper():
            correct_count += 1
            
    score_pct = (correct_count / len(quiz.questions)) * 100 if quiz.questions else 0
    
    result = QuizResult(
        user_id=current_user.id,
        quiz_id=quiz.id,
        score=score_pct,
        total_questions=len(quiz.questions)
    )
    db.session.add(result)
    db.session.commit()
    
    return render_template('quiz_result.html', quiz=quiz, score=score_pct, correct=correct_count, total=len(quiz.questions))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
