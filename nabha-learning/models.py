from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='student') # 'student' or 'teacher'
    grade = db.Column(db.Integer)  # class (5-10) for students; None for teachers
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    quiz_results = db.relationship('QuizResult', backref='student', lazy=True)

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    grade_level = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    units = db.relationship('Unit', backref='subject', cascade="all, delete-orphan", lazy=True)

class Unit(db.Model):
    __tablename__ = 'units'
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    unit_number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text)
    video_url = db.Column(db.String(300))

    quizzes = db.relationship('Quiz', backref='unit', cascade="all, delete-orphan", lazy=True)

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)

    questions = db.relationship('Question', backref='quiz', cascade="all, delete-orphan", lazy=True)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False) # 'A', 'B', 'C', 'D'

class QuizResult(db.Model):
    __tablename__ = 'quiz_results'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)


class TimetableEntry(db.Model):
    __tablename__ = 'timetable_entries'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)      # 0 = Monday ... 5 = Saturday
    period = db.Column(db.Integer, nullable=False)   # 1, 2, 3 ...
    subject_name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.String(5), nullable=False)  # "09:00"
    end_time = db.Column(db.String(5), nullable=False)    # "09:45"

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # 'present' or 'absent'
    marked_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    student = db.relationship('User', foreign_keys=[user_id], backref='attendance_records')
    __table_args__ = (db.UniqueConstraint('user_id', 'date', name='uq_attendance_user_date'),)
