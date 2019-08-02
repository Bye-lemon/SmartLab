#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 19:06
# @Author  : Li Yingping
# @File    : modelview.py
# @Software: PyCharm

# TODO: Export File Rename (Type + DateTime)

import tablib
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import typefmt

from .forms import ActivityForm, ActivityDetailForm


class ModalView(ModelView):
    create_modal = True
    details_modal = True
    edit_modal = True
    export_types = ['xls']

    column_type_formatters = dict(
        typefmt.BASE_FORMATTERS
    )


class UserView(ModalView):
    can_create = False
    can_edit = False
    can_delete = False
    can_export = True
    can_view_details = True

    column_labels = dict(
        user_id="学号",
        name="姓名",
        major="专业",
        email="邮箱",
        is_allowed="审核结果",
        role="身份",
        coin="积分"
    )
    column_display_pk = True
    column_descriptions = dict(
        is_allowed="审核通过的注册用户拥有实验室的学生权限。"
    )
    column_exclude_list = (
        'pwd_hash', 'avatar_hash', 'create_time', 'update_time'
    )
    column_export_exclude_list = (
        'pwd_hash', 'avatar_hash', 'create_time', 'update_time'
    )


class AuditView(ModalView):
    can_create = False
    can_edit = True
    can_delete = False
    can_export = True
    can_view_details = True

    column_labels = dict(
        user_id="学号",
        name="姓名",
        major="专业",
        email="邮箱",
        is_allowed="是否接受",
        role="身份",
        coin="积分"
    )
    column_descriptions = dict(
        is_allowed="审核通过的注册用户拥有实验室的学生权限。",
        is_deleted="被标记的注册用户将被系统忽视处理。"
    )
    column_exclude_list = (
        'pwd_hash', 'avatar_hash', 'email', 'create_time', 'update_time', 'email', 'coin'
    )
    column_export_exclude_list = (
        'pwd_hash', 'avatar_hash', 'create_time', 'update_time'
    )
    column_filters = (
        'is_allowed', 'role'
    )
    column_editable_list = (
        'role', 'is_allowed'
    )
    column_formatters = dict(
        is_allowed=lambda _, __, x, ___: "是" if x.is_allowed == 1 else "否",
        is_deleted=lambda _, __, x, ___: "是" if x.is_deleted == 1 else "否"
    )
    column_display_pk = True


class ToolView(ModalView):
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    can_view_details = True

    column_labels = dict(
        box_id="序号",
        name="名称",
        is_borrowed="是否被借用",
        user_id="借用人学号",
        create_time="登记时间",
        update_time="上次变动时间"
    )
    column_descriptions = dict(
        update_time="被借用的工具的借用时间或者被归还的工具的归还时间。"
    )
    column_filters = (
        'is_borrowed', 'user_id'
    )
    column_editable_list = (
        'name',
    )
    form_excluded_columns = (
        'is_borrowed', 'user_id', 'create_time', 'update_time'
    )
    column_formatters = dict(
        is_borrowed=lambda _, __, x, ___: "是" if x.is_borrowed == 1 else "否"
    )
    column_display_pk = True


class ManipulationView(ModalView):
    can_create = False
    can_edit = False
    can_delete = False
    can_export = True
    can_view_details = True

    column_labels = dict(
        manipulation_id="记录号",
        user_id="学生学号",
        time="记录时间",
        function_type="活动记录",
        box_id="工具号"
    )
    column_descriptions = dict(
        box_id="被借用或归还的工具的编号。"
    )
    column_formatters = dict(
        function_type=lambda _, __, x, ___: ["开门", "借用工具", "归还工具"][x.function_type - 1],
        box_id=lambda _, __, x, ___: None if x.box_id == 0 else x.box_id
    )


class UserActivityView(ModalView):
    can_create = False
    can_edit = False
    can_delete = False
    can_export = True
    can_view_details = True

    column_labels = dict(
        user_id="学生学号",
        activity_id="课程或活动号",
        is_complete="是否完成",
        score="成绩信息"
    )
    column_exclude_list = (
        'is_complete', 'score'
    )
    column_filters = (
        'activity_id',
    )
    column_display_pk = True


class GradeView(ModalView):
    can_create = False
    can_edit = True
    can_delete = False
    can_export = True
    can_view_details = True

    column_labels = dict(
        user_id="学生学号",
        activity_id="课程或活动号",
        is_complete="是否完成",
        score="成绩信息"
    )
    column_editable_list = (
        'score',
    )
    column_filters = (
        'activity_id',
    )
    column_display_pk = True


class ActivityView(ModalView):
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    can_view_details = True

    column_labels = dict(
        activity_id="编号",
        type="类别",
        status="是否开放",
        name="名称",
        rest_number="剩余可选人数",
        max_number="总容量",
        create_time="创建时间",
        update_time="上次变动时间",
        teacher="教师或主持人",
    )
    column_formatters = dict(
        type=lambda _, __, x, ___: ["课程", "活动"][x.type - 1],
        status=lambda _, __, x, ___: "是" if x.status == 1 else "否"
    )
    column_filters = (
        'status', 'teacher', 'type'
    )
    column_editable_list = (
        'status',
    )
    form = ActivityForm
    column_display_pk = True


class ActivityDetailView(ModalView):
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    can_view_details = True

    column_labels = dict(
        activity_detail_id="编号",
        week="周次",
        day="星期",
        activity_order="节次",
        location="活动地点",
        activity_id="活动号"
    )
    form = ActivityDetailForm
    form_widget_args = {
        "class": ""
    }
