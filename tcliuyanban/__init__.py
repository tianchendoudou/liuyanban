# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
@author: tianchen
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 1561422137@qq.com
@file: __init__.py
@time: 2020/6/29 3:27 下午
@desc:
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('tcliuyanban')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from tcliuyanban import views, errors, commands