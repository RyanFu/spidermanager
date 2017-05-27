# -*- coding: utf-8 -*-
import base64
import json

from flask import request, redirect, url_for, jsonify, session

from spidermanager import app,db
from spidermanager.model.user import User
from spidermanager.setting import managerhosts
from spidermanager.util.action_result import list2json, obj2json

from spidermanager.setting import basedir
from jinja2 import Template

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@app.route("/user/add", methods=['GET','POST'])
def add():

    username = request.form.get('username')
    description = request.form.get('description')
    password = request.form.get('password')
    type = request.form.get('type')
    status = request.form.get('status')
    if(status==None):
        status="stop"
    webuiport = request.form.get('webuiport')
    schedulerport = request.form.get('schedulerport')
    projectdb = request.form.get('projectdb')
    taskdb = request.form.get('taskdb')
    resultdb = request.form.get('resultdb')
    try:
        user = User(username, description, password, type, status, webuiport, schedulerport, projectdb, taskdb, resultdb)
        db.session.add(user)
        db.session.commit()
        resp = {
            "status":"ok",
            "detail":username
        }
    except Exception,e:
        print e
        resp = {
            "status":"error",
            "detail":"无法新增，可能相同ID已存在！"
        }

    return json.dumps(resp)


@app.route("/user/edit", methods=['GET','POST'])
def edit():

    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    user.description = base64.b64encode(request.form.get('description'))
    user.password = request.form.get('password')
    user.type = request.form.get('type')
    user.status = request.form.get('status')
    if(user.status==None):
        user.status="stop"
    user.webuiport = request.form.get('webuiport')
    user.schedulerport = request.form.get('schedulerport')
    user.projectdb = request.form.get('projectdb')
    user.taskdb = request.form.get('taskdb')
    user.resultdb = request.form.get('resultdb')
    try:
        db.session.commit()
        resp = {
            "status":"ok",
            "detail":username
        }
    except Exception,e:
        print e
        resp = {
            "status":"error",
            "detail":"无法修改！"
        }

    return json.dumps(resp)


@app.route("/user/delete", methods=['GET','POST'])
def delete():

    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()

    resp = {
        "status":"ok",
        "detail":username
    }

    return json.dumps(resp)


@app.route("/user/load", methods=['GET','POST'])
def load():
    users = db.session.query(User).all()

    for user in users:
        try:
            user.description = base64.b64decode(user.description)
        except Exception,e:
            print e

    return list2json(users)

@app.route("/user/get", methods=['GET','POST'])
def get():

    username = request.values.get('username')
    user = User.query.filter_by(username=username).first()
    try:
        user.description = base64.b64decode(user.description)
    except Exception,e:
        print e
    return obj2json(user)

@app.route("/user/getlink", methods=['GET','POST'])
def getlink():

    username = request.values.get('username')
    user = User.query.filter_by(username=username).first()
    managerhost = managerhosts[0]
    managerport = user.webuiport
    resp = {
        "link":"http://"+str(managerhost)+":"+str(managerport),
    }
    return json.dumps(resp)

@app.route("/user/start", methods=['GET','POST'])
def start():
    username = request.values.get('username')
    user_type = request.values.get('user_type')
    from spidermanager.service.remote_controller import RemoteController
    rc = RemoteController(username)
    rc.startall(user_type)
    user = User.query.filter_by(username=username).first()
    user.status = "running"
    try:
        db.session.commit()
        resp = {
            "status":"ok",
            "detail":username
        }
    except Exception,e:
        print e
        resp = {
            "status":"error",
            "detail":"无法修改！"
        }
    return json.dumps(resp)

@app.route("/user/setPhantomjs", methods=['GET','POST'])
def setPhantomjs():
    startport = request.values.get('startport')
    endport = request.values.get('endport')
    session['startport'] = startport
    session['endport'] = endport
    print startport,endport
    f0=open(basedir + "/templates/config.tpl.bak","r")
    str_f0 = f0.read()
    f0.close()
    tpl = Template(str_f0)    
    phantomjs_endpoint = ""
    ports = ""
    for i in range(int(startport),int(endport)+1):
        if i != int(session['endport']):
            phantomjs_endpoint = phantomjs_endpoint+"127.0.0.1:"+str(i)+","
            ports = ports+str(i)+","
        else:
            phantomjs_endpoint = phantomjs_endpoint+"127.0.0.1:"+str(i)
            ports = ports+str(i)
    config =  tpl.render(
        taskdb="{{ taskdb }}",
        projectdb="{{ projectdb }}",
        resultdb="{{ resultdb }}",
        schedulerhost="{{ schedulerhost }}",
        schedulerport="{{ schedulerport }}",
        username="{{ username }}",
        webuiport="{{ webuiport }}",
        password="{{ password }}",
        phantomjs_endpoint = phantomjs_endpoint,
        ports = ports
    )
    f1=open(basedir + "/templates/config.tpl","wb")
    f1.write(config)
    f1.close()
    from spidermanager.service.remote_controller import RemoteController
    rc = RemoteController("phantomjs")#Phantomjs日志文件phantomjs.log
    rc.stopPhantomjs()
    rc.startPhantomjs()
    resp = {
        "phantomjsPorts":+str(startport)+" to "+str(endport),
    }
    return json.dumps({})

@app.route("/user/stop", methods=['GET','POST'])
def stop():

    username = request.values.get('username')
    from spidermanager.service.remote_controller import RemoteController
    rc = RemoteController(username)
    rc.killall()
    user = User.query.filter_by(username=username).first()
    user.status = "stop"
    try:
        db.session.commit()
        resp = {
            "status":"ok",
            "detail":username
        }
    except Exception,e:
        print e
        resp = {
            "status":"error",
            "detail":"无法修改！"
        }
    return json.dumps(resp)


@app.route("/user/restart", methods=['GET','POST'])
def restart():

    username = request.values.get('username')
    user_type = request.values.get('user_type')
    from spidermanager.service.remote_controller import RemoteController
    rc = RemoteController(username)
    rc.killall()
    rc.startall(user_type)
    user = User.query.filter_by(username=username).first()
    user.status = "running"
    try:
        db.session.commit()
        resp = {
            "status":"ok",
            "detail":username
        }
    except Exception,e:
        print e
        resp = {
            "status":"error",
            "detail":"无法修改！"
        }
    return json.dumps(resp)
