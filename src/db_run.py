from db import db
from app import app
from models import Doctor


with app.app_context():
    db.drop_all()
    db.create_all()


with app.app_context():
    doctor = Doctor(age=45, second_name="Popov", first_name="Alexandr",
                    last_name="Vladimir", telephone="777777777", email="qqq@mail.ru",
                    profile="urolog", experience="20 years")
    db.session.add(doctor)
    doctor1 = Doctor(age=45, second_name="Popov", first_name="Alexandr",
                    last_name="Vladimir", telephone="777777777", email="qwwqq@mail.ru",
                    profile="urolog", experience="20 years")
    db.session.add(doctor1)
    db.session.commit()


with app.app_context():
    doctors = Doctor.query.all()
    for d in doctors:
        print(d.first_name, d.second_name, d.email)
