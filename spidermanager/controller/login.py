# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, session

from spidermanager import app
from spidermanager.model.admin import Admin
from spidermanager.model.user import User
from spidermanager.setting import managerhosts


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['form-username']
        password = request.form['form-password']
        try:
            return login_as_user(username, password)
        except Exception,e1:
            try:
                return login_as_admin(username, password)
            except Exception,e0:
                print e0
                return render_template('login.html', message='用户名或密码错误！')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

def login_as_user(username, password):
    user = User.query.filter_by(username=username).first()
    if(password == user.password):
        if user.status != 'running':
            return render_template('login.html', message='爬虫服务异常！请致电联系 齐希 13958112099 或 金星 13023660069')
        managerhost = managerhosts[0]
        managerport = user.webuiport
        link = "http://"+str(managerhost)+":"+str(managerport)
        return redirect(link)
    else:
        return render_template('login.html', message='用户名或密码错误！')


def login_as_admin(username, password):
    admin = Admin.query.filter_by(username=username).first()
    if(password == admin.password):
        session['admin'] = username
        return redirect(url_for('main'))
    else:
        return render_template('login.html', message='用户名或密码错误！')