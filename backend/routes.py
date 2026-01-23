from flask import Blueprint, request, jsonify, session, redirect, url_for, render_template
from models import db, User, Job, Application
import bcrypt
from functools import wraps

routes = Blueprint('routes', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('routes.login'))
        return f(*args, **kwargs)
    return decorated_function

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(username=data['username'], email=data['email'], password=hashed.decode('utf-8'), role=data['role'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('routes.login'))
    return render_template('register.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect(url_for('routes.dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@routes.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes.index'))

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    if user.role == 'employer':
        jobs = Job.query.filter_by(employer_id=user.id).all()
        return render_template('dashboard.html', jobs=jobs)
    else:
        applications = Application.query.filter_by(user_id=user.id).all()
        return render_template('dashboard.html', applications=applications)

@routes.route('/jobs', methods=['GET'])
def jobs():
    query = request.args.get('q', '')
    jobs = Job.query.filter(Job.title.contains(query)).all()
    return render_template('jobs.html', jobs=jobs)

@routes.route('/job/<int:job_id>')
def job_details(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job_details.html', job=job)

@routes.route('/post_job', methods=['GET', 'POST'])
@login_required
def post_job():
    if session['role'] != 'employer':
        return 'Unauthorized'
    if request.method == 'POST':
        data = request.form
        job = Job(title=data['title'], description=data['description'], company=data['company'],
                  location=data['location'], salary=data['salary'], employer_id=session['user_id'])
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('routes.dashboard'))
    return render_template('post_job.html')

@routes.route('/apply/<int:job_id>', methods=['POST'])
@login_required
def apply(job_id):
    if session['role'] != 'job_seeker':
        return 'Unauthorized'
    application = Application(job_id=job_id, user_id=session['user_id'])
    db.session.add(application)
    db.session.commit()
    return redirect(url_for('routes.jobs'))

@routes.route('/profile')
@login_required
def profile():
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)