from src.db import db

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

    second_name = db.Column(db.String(50))  # фамилия
    first_name = db.Column(db.String(50), nullable=False)  # имя
    last_name = db.Column(db.String(50))  # отчество

    telephone = db.Column(db.String(20), nullable=False)  # телефон
    email = db.Column(db.String(50), nullable=False, unique=True)  # мыло

    profile = db.Column(db.String(50), nullable=False)  # профиль
    experience = db.Column(db.String(10))  # опыт работы

    def __repr__(self):
        return (f"< Фамилия: {self.second_name}, Имя: {self.first_name}, Отчество: {self.last_name},"
                f" телефон: {self.telephone}, профиль: {self.profile}, опыт работы: {self.experience}>")


class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer(), primary_key=True)

    name_service = db.Column(db.String(100))  # наименование услуги
    description = db.Column(db.Text())  # описание услуги
    executor = db.Column(db.String(50))  # исполнитель
    price = db.Column(db.Float())  # цена
    service_group_id = db.Column(db.ForeignKey("service_group.id"))  # id группы, к которой относится эта услуга
    service_group = db.Relationship("ServiceGroup")  # ссылка на группу(id которой указан в вышестоящей строчке)
    def __repr__(self):
        return (f"<Наименование услуги: {self.name_service} описание услуги: {self.description} "
                f"ответственный: {self.executor} цена: {self.price}>")



class ServiceGroup(db.Model):
    __tablename__ = "service_group"
    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(100))  # название группы
    description = db.Column(db.Text())  # описание группы
    # создать руководителя группы
    def __repr__(self):
        return f"<сервисная группа: {self.name}, описание группы: {self.description}>"
