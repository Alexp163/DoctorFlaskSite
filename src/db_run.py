from db import db
from app import app
from models import Doctor, Service


with app.app_context():
    db.drop_all()
    db.create_all()


with app.app_context():
    doctor = Doctor(age=45, second_name="Popov", first_name="Alexandr",
                    last_name="Vladimir", telephone="777777777", email="qqq@mail.ru",
                    profile="urolog", experience="20 years")
    db.session.add(doctor)
    doctor1 = Doctor(age=45, second_name="Sidorov", first_name="Igor",
                    last_name="Vladimir", telephone="7999999999", email="sidor@mail.ru",
                    profile="travmatolog", experience="10 years")
    db.session.add(doctor1)
    db.session.commit()


with app.app_context():
    service = Service(name_service = "Общий анализ крови", description =
                    "эритроциты, лейкоциты и тромбоциты крови",
                      executor = "врач-лаборант Соколов И.И.",
                      price = "510.00", service_grope_name = "лабораторные исследования")
    db.session.add(service)
    service1 = Service(name_service = "МРТ головного мозга", description =
                    "описание структур головного мозга",
                      executor = "врач-рентгенолог Постовский Р.В.",
                      price = "17510.00", service_grope_name = "рентгенологические исследования")

