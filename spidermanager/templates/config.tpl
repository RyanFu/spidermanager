{
  "taskdb": "sqlalchemy+oracle+taskdb://{{ taskdb }}",
  "projectdb":"sqlalchemy+oracle+projectdb://{{ projectdb }}",
  "resultdb": "sqlalchemy+oracle+resultdb://{{ resultdb }}",
  "scheduler":{
    "xmlrpc-host":"{{ schedulerhost }}",
    "xmlrpc-port":"{{ schedulerport }}"
  },
  "message_queue": "redis://20.26.26.43:6379/db",
  "fetcher":{
  "phantomjs-endpoint":"127.0.0.1:25550,127.0.0.1:25551,127.0.0.1:25552"
  },
  "queue_user": "{{ username }}",
  "webui": {
    "scheduler-rpc":"http://{{ schedulerhost }}:{{ schedulerport }}",
    "port":"{{ webuiport }}",
    "username": "{{ username }}",
    "password": "{{ password }}",
    "need-auth": true
  }
   "phantomjs": {
   "phantomjs-path":"/home/spd/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",
   "ports": "25550,25551,25552"
  }
}