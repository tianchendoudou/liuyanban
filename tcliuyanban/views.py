# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
@author: tianchen
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 1561422137@qq.com
@file: views.py
@time: 2020/6/29 4:20 下午
@desc:
'''
from flask import flash,redirect,url_for,render_template
from tcliuyanban import app,db
from tcliuyanban.model import Message
from tcliuyanban.forms import HelloForm

@app.route('/',methods=['GET','POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body,name=name)#构建数据实体
        db.session.add(message)#添加记录
        db.session.commit()#提交回话完成数据写入
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))#重定向index
    return render_template('index.html',form=form,messages=messages)

