# coding=utf-8
from flask_admin import Admin
from flask_babelex import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name="SmartLab 教师管理后台", template_mode="bootstrap3")
babel = Babel()


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    user = User.query.get(user_id)
    return user
