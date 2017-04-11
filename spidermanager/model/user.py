# -*- coding: utf-8 -*-


from sqlalchemy import Column, String, INTEGER

from spidermanager import db


class User(db.Model):
    __tablename__ = 'USER'
    username = Column(String(32), primary_key=True)
    description = Column(String(256))
    password = Column(String(64))
    type = Column(String(32))
    status = Column(String(32))
    webuiport = Column(INTEGER, unique=True)
    schedulerport = Column(INTEGER, unique=True)
    projectdb = Column(String(512))
    taskdb = Column(String(512))
    resultdb = Column(String(512))

    def __init__(self, username=None, description=None, password=None, type=None, status=None, webuiport=None, schedulerport=None, projectdb=None, taskdb=None, resultdb=None):
        self.username = username
        self.description = description
        self.password = password
        self.type = type
        self.status = status
        self.webuiport = webuiport
        self.schedulerport = schedulerport
        self.projectdb = projectdb
        self.taskdb = taskdb
        self.resultdb = resultdb

    def __repr__(self):
        return '<User %r>' % (self.username)