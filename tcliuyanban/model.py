# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
@author: tianchen
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 1561422137@qq.com
@file: model.py
@time: 2020/6/29 3:37 下午
@desc:
'''
from datetime import datetime

from tcliuyanban import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
