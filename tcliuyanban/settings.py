# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
@author: tianchen
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 1561422137@qq.com
@file: settings.py
@time: 2020/6/29 3:27 下午
@desc:
'''

import os
import sys

from tcliuyanban import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'tcdata.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)