# -*- coding: utf-8 -*-
import os

#调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_NATIVE_UNICODE = True

SECRET_KEY= 'ty@puton.info'


try:
    PROFILE = os.environ["SPD_PROFILE"]
except Exception,e:
    PROFILE = 'dev'


if PROFILE == 'dev':
    basedir='D:/Git/pyspider/git/spidermanager/spidermanager'
    spdmgrport=5000
    managerhosts = ['master.hadoop']
    workerhosts= ['slave1.hadoop','slave2.hadoop']
    #SQLALCHEMY_DATABASE_URI = "oracle://spdmgr:spdmgr_1Q#@oracle-datasource:1521/pdbspdmgr"
    SQLALCHEMY_DATABASE_URI = "oracle://SCOTT:gb666666@localhost:1521/ORCL"
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://app:123456@localhost:3306/spdmgr"
    redis_nodes =  [{'host':'192.168.136.130','port':7000},
                    {'host':'192.168.136.130','port':7001},
                    {'host':'192.168.136.130','port':7002},
                    {'host':'192.168.136.131','port':7000},
                    {'host':'192.168.136.131','port':7001},
                    {'host':'192.168.136.131','port':7002},
                    ]
    redis_expires = 30
    landing = []
    hbase_host = 'master.hadoop'
    hbase_port = 9090
    accessid = ''
    accesskey = ''
    es_host = ["master.hadoop"]
    hdfs_web = "http://master.hadoop:50070"
    hdfs_dir = "/user/spider/cplatform/"
    hdfs_user = "hadoop"

elif PROFILE == 'test':
    log_dir_master="/home/spd/spidermanager/runtime/log"
    log_dir_slave = "/home/spd/spidermanager/runtime/log"
    spdmgrport=5888
    basedir='/home/spd/spidermanager/server/spidermanager'
    managerhosts = ['20.26.26.43']
    workerhosts = ['20.26.25.224','20.26.25.225']
    SQLALCHEMY_DATABASE_URI = "oracle://pyspd_admin:pyspd_admin_1Q#@pdb_bdprd"
    redis_nodes =  [{'host':'20.26.25.224','port':7000},
                    {'host':'20.26.25.224','port':7001},
                    {'host':'20.26.25.224','port':7002},
                    {'host':'20.26.25.225','port':7000},
                    {'host':'20.26.25.225','port':7001},
                    {'host':'20.26.25.225','port':7002},
                    ]
    redis_expires = 86400
    # persist = ["hbase","hdfs","es"]
    landing = []
    hbase_host = '10.78.138.74'
    hbase_port = 9090
    accessid = '480092febea017febfe4'
    accesskey = '3fe3bccd97e3c8cb9c5b57cffc74090671722641'
    es_host = ["10.78.138.53",
               "10.78.138.54",
               "10.78.138.55",
               "10.78.138.56",
               "10.78.138.57",
               "10.78.138.58",
               "10.78.138.59",
               "10.78.138.60",
               "10.78.138.61",
               "10.78.138.62",
               "10.78.138.63",
               "10.78.138.64",
               "10.78.138.65",
               "10.78.138.66",
               "10.78.138.67",
               "10.78.138.68",
               "10.78.138.69",
               "10.78.138.70",
               "10.78.138.71",
               "10.78.138.72",
               ]
    hdfs_web = "http://10.78.138.81:50070"
    hdfs_dir = "/user/spider/cplatform/"
    hdfs_user = "hadoop"


elif PROFILE == 'prod':
    log_dir_master = "/data/log"
    log_dir_slave="/srv/BigData/data1/log/univider/pyspider_log"
    spdmgrport=5000
    basedir='/home/spd/spidermanager/server/spidermanager'
    managerhosts = ['10.78.238.55']
    workerhosts = ['10.78.190.229','10.78.190.230','10.78.190.231','10.78.190.232','10.78.190.233','10.78.190.234','10.78.190.235']
    SQLALCHEMY_DATABASE_URI = "oracle://spd_admin:spd_admin_1Q#@pdb_spider"
    redis_nodes =  [{'host':'10.78.155.61','port':16340},
                    {'host':'10.78.155.67','port':16340},
                    {'host':'10.78.155.68','port':16340},
                    {'host':'10.78.155.70','port':16340},
                    {'host':'10.78.155.71','port':16340},
                    {'host':'10.78.155.72','port':16340},
                    ]
    redis_expires = 86400
    # persist = ["hbase","hdfs","es"]
    landing = []
    hbase_host = '10.78.138.74'
    hbase_port = 9090
    accessid = '480092febea017febfe4'
    accesskey = '3fe3bccd97e3c8cb9c5b57cffc74090671722641'
    es_host = ["10.78.138.53",
               "10.78.138.54",
               "10.78.138.55",
               "10.78.138.56",
               "10.78.138.57",
               "10.78.138.58",
               "10.78.138.59",
               "10.78.138.60",
               "10.78.138.61",
               "10.78.138.62",
               "10.78.138.63",
               "10.78.138.64",
               "10.78.138.65",
               "10.78.138.66",
               "10.78.138.67",
               "10.78.138.68",
               "10.78.138.69",
               "10.78.138.70",
               "10.78.138.71",
               "10.78.138.72",
               ]
    hdfs_web = "http://10.78.138.81:50070"
    hdfs_dir = "/user/spider/cplatform/"
    hdfs_user = "hadoop"


