from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, \
    Float
from sqlalchemy.orm import Relationship
from sqlalchemy.sql import func

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

    id = Column(Integer(), primary_key=True)
    age = Column(Integer())

    second_name = Column(String(50))  # фамилия
    first_name = Column(String(50), nullable=False)  # имя
    last_name = Column(String(50))  # отчество

    telephone = Column(String(20), nullable=False)  # телефон
    email = Column(String(50), nullable=False, unique=True)  # мыло

    profile = Column(String(50), nullable=False)  # профиль
    experience = Column(String(10))  # опыт работы

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"< Фамилия: {self.second_name}, Имя: {self.first_name}, Отчество: {self.last_name},"
                f" телефон: {self.telephone}, профиль: {self.profile}, опыт работы: {self.experience}>")




class Service(db.Model):
    __tablename__ = "service"

    id = Column(Integer(), primary_key=True)

    name_service = Column(String(100))  # наименование услуги
    description = Column(Text())  # описание услуги
    executor = Column(String(50))  # исполнитель
    price = Column(Float())  # цена
    service_group_id = Column(ForeignKey("service_group.id"))  # id группы, к которой относится эта услуга
    service_group = Relationship("ServiceGroup")  # ссылка на группу(id которой указан в вышестоящей строчке)

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    doctor_id = Column(ForeignKey("doctor.id"))
    doctor = Relationship("Doctor")

    def __repr__(self):
        return (f"<Наименование услуги: {self.name_service} описание услуги: {self.description} "
                f"ответственный: {self.executor} цена: {self.price}>")



class ServiceGroup(db.Model):
    __tablename__ = "service_group"
    id = Column(Integer(), primary_key=True)

    name = Column(String(100))  # название группы
    description = Column(Text())  # описание группы

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    doctor_id = Column(ForeignKey("doctor.id"))
    doctor = Relationship("Doctor")

    # создать руководителя группы
    def __repr__(self):
        return f"<сервисная группа: {self.name}, описание группы: {self.description}>"


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)

    nick_name = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password_hash = Column(String(256))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    def __repr__(self):
        return f"<Email: {self.email}, Никнэйм: {self.nick_name}>"
