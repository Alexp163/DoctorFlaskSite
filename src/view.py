from app import app
from flask import render_template
from models import Service, Doctor, ServiceGroup
from forms import LoginForm, RegisterForm


@app.route('/')
def index():
    service_groups = ServiceGroup.query.all()
    return render_template('index.html', service_groups=service_groups)


@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/registration')
def registration():
    form = RegisterForm()
    return render_template('registration.html', form=form)


@app.route('/doctors/<int:doctor_id>')
def one_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    return render_template('one_doctor.html', doctor=doctor)


@app.route('/service/')
def service():
    service = Service.query.all()
    return render_template('analyzes.html', service=service)


@app.route('/service_group/<int:service_group_id>')
def service_group(service_group_id):
    service_group = ServiceGroup.query.get(service_group_id)
    service_groups = ServiceGroup.query.all()
    service = Service.query.filter_by(service_group_id=service_group_id).all()
    return render_template("service_group.html", service_group=service_group,
                           service=service, service_groups=service_groups)
