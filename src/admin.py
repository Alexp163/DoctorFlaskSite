from flask_admin import Admin
from app import app
from flask_admin.contrib.sqla import ModelView
from models import Doctor, Service, ServiceGroup, User
from db import db


admin = Admin(app, __name__, template_mode="bootstrap3")

class DoctorModelView(ModelView):
    column_list = ('telephone', 'last_name', 'second_name', 'age', 'first_name',
                   'email', 'profile', 'experience', 'created_at', 'updated_at' )
    form_excluded_columns = ('created_at', 'updated_at')  # исключиредактирование даты создания и даты обновления


class ServiceModelView(ModelView):
    column_list = ('name_service', 'description', 'price', 'service_group', 'doctor')
    form_excluded_columns = ('created_at', 'updated_at')  # исключиредактирование даты создания и даты обновления


class ServiceGroupModelView(ModelView):
    column_list = ('name', 'description', 'doctor')
    form_excluded_columns = ('created_at', 'updated_at')  # исключиредактирование даты создания и даты обновления


class UserModelView(ModelView):
    column_list = ('nick_name', 'email')
    form_excluded_columns = ('created_at', 'updated_at', 'password_hash')

admin.add_view(DoctorModelView(Doctor, db.session))
admin.add_view(ServiceModelView(Service, db.session))
admin.add_view(ServiceGroupModelView(ServiceGroup, db.session))
admin.add_view(UserModelView(User, db.session))





