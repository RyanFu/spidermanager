# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#加载配置文件内容
app.config.from_object('spidermanager.setting')     #模块下的setting文件名，不用加py后缀
# app.config.from_envvar('SPIDERMANAGER_SETTING')   #环境变量，指向配置文件setting的路径

#创建数据库对象
db = SQLAlchemy(app)