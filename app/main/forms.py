# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



# Name Form
class NameForm(Form):
    # DataRequired instead of Required
    name = StringField(u'可以告诉谦虚的我, 您叫什么名字吗?', validators=[DataRequired()])
    submit = SubmitField(u'既然你这么谦虚, 告诉你吧!')