# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
@author: tianchen
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 1561422137@qq.com
@file: forms.py
@time: 2020/6/29 4:13 下午
@desc:
'''
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class HelloForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(),Length(1,20)])
    body = TextAreaField('Message',validators=[DataRequired(),Length(1,200)])
    submit = SubmitField()
