# coding=utf-8
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

from app.admin.modelview import UserView, ModalView
from app.extensions import admin, db
from app.models import Activity, ActivityDetail, Manipulation, Tool, User, UserActivity

admin.add_view(ModalView(User, db.session, category="人员管理", name="注册信息"))
admin.add_view(ModalView(User, db.session, category="人员管理", name="审核申请", endpoint="/audit"))
admin.add_view(ModalView(Tool, db.session, name="物品管理"))
admin.add_view(ModalView(Activity, db.session, category="活动与课程管理", name="添加课程记录"))
admin.add_view(ModalView(ActivityDetail, db.session, category="活动与课程管理", name="补全课程信息"))
admin.add_view(ModalView(UserActivity, db.session, category="活动与课程管理", name="查看选课情况"))
admin.add_view(ModalView(Manipulation, db.session, name="实验室活动日志"))
admin.add_view(FileAdmin(op.join(op.dirname(op.dirname(__file__)), 'static', 'resource'), name='文件上传'))
