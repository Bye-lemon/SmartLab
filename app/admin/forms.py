#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 14:04
# @Author  : Li Yingping
# @File    : forms.py
# @Software: PyCharm
from flask_admin.form import BaseForm
from flask_admin.form.fields import Select2Field
from wtforms import IntegerField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

from .compatibility import SelectMultipleField


class ActivityForm(BaseForm):
    type = Select2Field(
        label="类别",
        coerce=int,
        choices=[
            (1, "课程"),
            (2, "活动")
        ],
        validators=[DataRequired()]
    )
    status = Select2Field(
        label="是否默认开放",
        coerce=int,
        choices=[
            (0, "否"),
            (1, "是")
        ],
        validators=[DataRequired()]
    )
    name = StringField(
        label="名称",
        validators=[
            DataRequired(),
            Length(0, 255)
        ]
    )
    max_number = IntegerField(
        label="总容量",
        validators=[DataRequired()]
    )
    rest_number = IntegerField(
        label="剩余容量",
        validators=[DataRequired()]
    )
    teacher = StringField(
        label="教师或主持人",
        validators=[
            DataRequired(),
            Length(0, 255)
        ]
    )


class ActivityDetailForm(BaseForm):
    week = SelectMultipleField(
        label="周次",
        coerce=int,
        choices=[
            (1, "第一周"),
            (2, "第二周"),
            (3, "第三周"),
            (4, "第四周"),
            (5, "第五周"),
            (6, "第六周"),
            (7, "第七周"),
            (8, "第八周"),
            (9, "第九周"),
            (10, "第十周"),
            (11, "第十一周"),
            (12, "第十二周"),
            (13, "第十三周"),
            (14, "第十四周"),
            (15, "第十五周"),
            (16, "第十六周"),
            (17, "第十七周"),
            (18, "第十八周"),
            (19, "第十九周")
        ],
        validators=[DataRequired()]
    )
    day = SelectMultipleField(
        label="星期",
        coerce=int,
        choices=[
            (1, "星期一"),
            (2, "星期二"),
            (3, "星期三"),
            (4, "星期四"),
            (5, "星期五"),
            (6, "星期六"),
            (7, "星期日")
        ],
        validators=[DataRequired()]
    )
    activity_order = SelectMultipleField(
        label="节次",
        coerce=int,
        choices=[
            (1, "第一节"),
            (2, "第二节"),
            (3, "第三节"),
            (4, "第四节"),
            (5, "第五节"),
            (6, "第六节"),
            (7, "第七节"),
            (8, "第八节"),
            (9, "第九节"),
            (10, "第十节"),
            (11, "第十一节")
        ],
        validators=[DataRequired()]
    )
    location = StringField(
        label="活动地点",
        validators=[
            DataRequired(),
            Length(0, 255)
        ]
    )
    activity_id = IntegerField(
        label="活动号",
        validators=[DataRequired()]
    )
