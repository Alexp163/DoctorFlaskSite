from app import app
from flask import render_template
from models import Service, Doctor



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


@app.route('/doctors/<int:doctor_id>')
def one_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    return render_template('one_doctor.html', doctor=doctor)


@app.route('/service/')
def service():
    service = Service.query.all()
    return render_template('analyzes.html', service=service)
