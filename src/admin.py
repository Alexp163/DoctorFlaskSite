from flask_admin import Admin
from app import app
from flask_admin.contrib.sqla import ModelView
from models import Doctor, Service, ServiceGroup
from db import db


admin = Admin(app, __name__, template_mode="bootstrap3")

class DoctorModelView(ModelView):
    column_list = ('telephone', 'last_name', 'second_name', 'age', 'first_name',
                   'email', 'profile', 'experience', 'created_at', 'updated_at' )
    form_excluded_columns = ('created_at', 'updated_at')


class ServiceModelView(ModelView):
    column_list = ('name_service', 'description', 'executor', 'price', 'service_group')
    form_excluded_columns = ('created_at', 'updated_at')

admin.add_view(DoctorModelView(Doctor, db.session))
admin.add_view(ServiceModelView(Service, db.session))
admin.add_view(ModelView(ServiceGroup, db.session))





