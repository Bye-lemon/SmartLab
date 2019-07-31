# coding=utf-8
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

from app.admin.modelview import UserView, MyView
from app.extensions import admin, db
from app.models import Users, Activities, Powerbars, Boxes

admin.add_view(UserView(Users, db.session, name="人员管理"))
admin.add_view(ModelView(Activities, db.session, name="课程管理"))
admin.add_view(ModelView(Powerbars, db.session, category="工具管理", name="插排管理"))
admin.add_view(ModelView(Boxes, db.session, category="工具管理", name="格子管理"))
admin.add_view(FileAdmin(op.join(op.dirname(op.dirname(__file__)), 'static', 'resource'), name='文件上传'))
