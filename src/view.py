from app import app
from flask import render_template
from db_run import Doctor



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/doctors/1')
def one_doctor():
    return render_template('one_doctor.html')
