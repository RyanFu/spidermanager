# -*- coding: utf-8 -*-
import os

from jinja2 import Template

from spidermanager.model.user import User
from spidermanager.setting import basedir

from flask import request, redirect, url_for, jsonify, session


def generate_config(username):

    filename = basedir + "/tmp/"+ username +".json"

    f0=open(basedir + "/templates/config.tpl","r")

    str = f0.read()

    f0.close()

    tpl = Template(str)

    user = User.query.filter_by(username=username).first()
    
    phantomjs_endpoint = ""
    ports = ""
    for i in range(int(session['startport']),int(session['endport'])+1):
        if i != int(session['endport']):
            phantomjs_endpoint = phantomjs_endpoint+"127.0.0.1:"+str(i)+","
            ports = ports+str(i)+","
        else:
            phantomjs_endpoint = phantomjs_endpoint+"127.0.0.1:"+str(i)
            ports = ports+str(i)

    config =  tpl.render(
        taskdb=user.taskdb,
        projectdb=user.projectdb,
        resultdb=user.resultdb,
        schedulerhost="127.0.0.1",
        schedulerport=user.schedulerport,
        username=user.username,
        webuiport=user.webuiport,
        password=user.password,
        phantomjs_endpoint = phantomjs_endpoint,
        ports = ports
    )


    if os.path.exists(filename):
      os.remove(filename)

    f1=open(filename,"wb")

    f1.write(config)

    f1.close()

    return filename

# generate_config("aaaaaaaa")







