# -*- coding: utf-8 -*-
import json


def list2json(objList):
    if(objList!=None):
        dictList = []
        for obj in objList:
            objDict = obj.__dict__
            del objDict['_sa_instance_state']
            dictList.append(objDict)
        return json.dumps(dictList)
    else:
        return "[]"


def obj2json(obj):
    if(obj!=None):
        rowDict = obj.__dict__
        del rowDict['_sa_instance_state']
        return json.dumps(rowDict)
    else:
        return "{}"