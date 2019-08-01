#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 16:17
# @Author  : Li Yingping
# @File    : new.py
# @Software: PyCharm

from wtforms import widgets
from wtforms.fields import SelectField


class SelectMultipleField(SelectField):
    """
    No different from a normal select field, except this one can take (and
    validate) multiple choices.  You'll need to specify the HTML `size`
    attribute to the select field when rendering.
    """

    widget = widgets.Select(multiple=True)

    def iter_choices(self):
        for value, label in self.choices:
            selected = self.data is not None and self.coerce(value) in self.data
            yield (value, label, selected)

    def process_data(self, value):
        try:
            self.data = list(self.coerce(v) for v in value)
        except (ValueError, TypeError):
            self.data = None

    def process_formdata(self, valuelist):
        try:
            data = list(self.coerce(x) for x in valuelist)
            self.data = ','.join(list(map(str, data))).encode('ascii')
        except ValueError:
            raise ValueError(
                self.gettext(
                    "Invalid choice(s): one or more data inputs could not be coerced"
                )
            )

    def pre_validate(self, form):
        if self.data:
            values = list(c[0] for c in self.choices)
            for d in self.data:
                if d not in values:
                    pass