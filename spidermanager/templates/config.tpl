{
  "taskdb": "{{ taskdb }}",
  "projectdb":"{{ projectdb }}",
  "resultdb": "{{ resultdb }}",
  "scheduler":{
    "xmlrpc-host":"{{ schedulerhost }}",
    "xmlrpc-port":"{{ schedulerport }}"
  },
  "message_queue": "redis://20.26.26.43:6379/db",
  "phantomjs-proxy": "127.0.0.1:25555",
  "queue_user": "{{ username }}",
  "webui": {
    "scheduler-rpc":"http://{{ schedulerhost }}:{{ schedulerport }}",
    "port":"{{ webuiport }}",
    "username": "{{ username }}",
    "password": "{{ password }}",
    "need-auth": true
  }
}