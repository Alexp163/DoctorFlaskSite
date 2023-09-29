from app import app
from flask import render_template



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doctors')
def doctors():
    return render_template('doctors.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')
