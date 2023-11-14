from db import db
from app import app
from models import Doctor, Service, ServiceGroup

with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    doctor = Doctor(age=45, second_name="Popov", first_name="Alexandr",
                    last_name="Vladimir", telephone="777777777",
                    email="qqq@mail.ru",
                    profile="urolog", experience="20 years")
    db.session.add(doctor)
    doctor1 = Doctor(age=45, second_name="Sidorov", first_name="Igor",
                     last_name="Vladimir", telephone="7999999999",
                     email="sidor@mail.ru",
                     profile="travmatolog", experience="10 years")
    db.session.add(doctor1)
    db.session.commit()

with app.app_context():
    group1 = ServiceGroup(name="Консультации врачей",
                          description="Здесь будет описана группа")
    group2 = ServiceGroup(name="Методы исследования",
                          description="Здесь будет описана группа")
    group3 = ServiceGroup(name="Анализы",
                          description="Здесь будет описана группа")
    group4 = ServiceGroup(name="Лечение",
                          description="Здесь будет описана группа")
    db.session.add(group1)
    db.session.add(group2)
    db.session.add(group3)
    db.session.add(group4)
    db.session.commit()
    service = Service(name_service="Общий анализ крови", description=
    "эритроциты, лейкоциты и тромбоциты крови",
                      executor="врач-лаборант Соколов И.И.",
                      price="510.00", service_group=group3)
    db.session.add(service)
    service1 = Service(name_service="МРТ головного мозга", description=
    "описание структур головного мозга",
                       executor="врач-рентгенолог Постовский Р.В.",
                       price="17510.00", service_group = group2)
    db.session.add(service1)
    service2 = Service(name_service="Консультация хирурга", description=
    "осмотр, постановка диагноза и подбор метода лечения",
                       executor="врач-хирург Козлов А.В.",
                       price="2510.00", service_group = group1)
    db.session.add(service2)
    service3 = Service(name_service="Холецистэктомия", description=
    "удаление желчного пузыря с конкрементами",
                       executor="врач-хирург Сытыйгад Р.С.",
                       price="187510.00", service_group = group4)
    db.session.add(service3)
    service4 = Service(name_service="Биохимический анализ крови",
                       description="Биллирубин, АЛАТ, АСАТ, мочевина",
                       executor="врач-лаборант Лобов М.М.", price="3000.00",
                       service_group = group3)
    db.session.add(service4)
    db.session.commit()

