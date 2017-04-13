# -*- coding: utf-8 -*-
import os
import sys

path = os.path.abspath('../../../spidermanager')
sys.path.append(path)

from spidermanager import db

from spidermanager.model import user

db.create_all()