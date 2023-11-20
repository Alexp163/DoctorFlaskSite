from flask_admin import Admin
from src.app import app
from flask_admin.contrib.sqla import ModelView
from src.models import Doctor, Service, ServiceGroup
from src.db import db


admin = Admin(app, __name__, template_mode="bootstrap3")

admin.add_view(ModelView(Doctor, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(ServiceGroup, db.session))
