# -*- coding: utf-8 -*-


from spidermanager import db

from spidermanager.model import user, admin
from spidermanager.model.admin import Admin

db.create_all()

try:
    default_admin = Admin('admin', 'default_admin', 'spidermanager2017')
    db.session.add(default_admin)
    db.session.commit()
except Exception,e:
    print e
