# -*- coding: utf-8 -*-


from sqlalchemy import Column, String

from spidermanager import db


class Admin(db.Model):
    __tablename__ = 'ADMIN'
    username = Column(String(32), primary_key=True)
    description = Column(String(256))
    password = Column(String(64))


    def __init__(self, username=None, description=None, password=None):
        self.username = username
        self.description = description
        self.password = password


    def __repr__(self):
        return '<Admin %r>' % (self.username)