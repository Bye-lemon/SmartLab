from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ApkUploadForm(FlaskForm):
    apk = FileField(u'安装包', validators=[FileRequired(), FileAllowed(['apk'])])
    version = StringField(u'版本号', validators=[DataRequired()])
    date_version = StringField(u'日期版本号', validators=[DataRequired()])
    submit = SubmitField(u'上传安装包')
