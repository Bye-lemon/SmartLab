#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 19:06
# @Author  : Li Yingping
# @File    : modelview.py
# @Software: PyCharm

from flask_admin.contrib.sqla import ModelView

from app.models import User


class ModalView(ModelView):
    create_modal = True
    details_modal = True
    edit_modal = True


class UserView(ModalView):
    can_export = True
    column_labels = dict(
        name="姓名",
        id="学号",
        password="密码",
        phoneNumber="手机号码",
        isAllowed="审核结果"
    )
    column_descriptions = dict(
        isAllowed="审核通过的注册用户拥有实验室的学生权限。"
    )
    column_exclude_list = (
        'password'
    )
    column_export_exclude_list = (
        'password'
    )
    column_searchable_list = (
        'name',
        'id'
    )
    column_editable_list = (
        'phoneNumber',
        'isAllowed'
    )
    column_display_pk = True
