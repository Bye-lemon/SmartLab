# coding=utf-8
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

from app.admin.modelviews import UserView, ModalView, AuditView, ToolView, ManipulationView, GradeView, \
    UserActivityView, ActivityView, ActivityDetailView
from app.extensions import admin, db
from app.models import Activity, ActivityDetail, Manipulation, Tool, User, UserActivity

admin.add_view(UserView(User, db.session, category="人员管理", name="注册信息", endpoint="user"))
admin.add_view(AuditView(User, db.session, category="人员管理", name="审核申请", endpoint="audit"))
admin.add_view(ToolView(Tool, db.session, name="物品管理", endpoint="tool"))
admin.add_view(ActivityView(Activity, db.session, category="活动与课程管理", name="添加课程记录"))
admin.add_view(ActivityDetailView(ActivityDetail, db.session, category="活动与课程管理", name="补全课程信息"))
admin.add_view(UserActivityView(UserActivity, db.session, category="活动与课程管理", name="查看选课信息", endpoint="useractivity"))
admin.add_view(GradeView(UserActivity, db.session, category="活动与课程管理", name="课程成绩录入", endpoint="grade"))
admin.add_view(ManipulationView(Manipulation, db.session, name="实验室活动日志"))
admin.add_view(FileAdmin(op.join(op.dirname(op.dirname(__file__)), 'static', 'resource'), name='文件上传'))
