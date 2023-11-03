from db import db

# id - (число)
# first_name - имя (текст)
# second_name - фамилия (текст)
# last_name - отчество (текст)
# profile - профиль (текст)
# experience - опыт (число)
# age - возраст (число)
# telephone - телефон (текст)
# email - почта (текст)
# db.String(50) - текстовое поле заданной длины
# db.Integer() - числовое поле
# db.Column() - создания колонки (дополнительные поля nullable, unique, primary_key)
# для id всегда задается primary_key=True

class Doctor(db.Model):
    __tablename__ = "doctor"

    id = db.Column(db.Integer(), primary_key=True)
    age = db.Column(db.Integer())

    second_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))

    telephone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    profile = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.String(10))


class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer(), primary_key=True)

    name_service = db.Column(db.String(100))  # наименование услуги
    description = db.Column(db.Text())  # описание услуги
    executor = db.Column(db.String(50))  # исполнитель
    price = db.Column(db.Float())  # цена
    service_grope_name = db.Column(db.String(50))  # из какой группы услуга




