# -*- coding: utf-8 -*-

import paramiko

from spidermanager.setting import managerhosts, workerhosts,log_dir_slave,log_dir_master


allhosts = managerhosts + workerhosts
port = 22
username = 'spd'
password = 'py_spd'
base_dir = "/home/"+ username + "/spidermanager"
runtime_dir = base_dir + "/runtime"
log_dir = base_dir + "/log"
engine_pyspider_dir = "/home/"+ username + "/spidermanager/engine/pyspider"
command0 = "source /etc/profile; source ~/.bash_profile; "


class RemoteController:

    def __init__(self, user):
        self.user = user
        self.log_path_slave = log_dir_slave + "/" + user + ".log"
        self.log_path_master=log_dir_master + "/" + user + ".log"
        self.config_path = runtime_dir+"/"+user+".json"

    def mkconfigdir(self, hostname, username, password):
        command = 'mkdir -p ' + runtime_dir
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command=command)
        print stderr.read()
        print stdout.read()
        ssh.close()

    # mkconfigdir(hostname, username, password)

    def mklogdir(self, hostname, username, password):
        command = 'mkdir -p ' + log_dir
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command=command)
        print stderr.read()
        print stdout.read()
        ssh.close()

    # mklogdir(hostname, username, password)


    def uploadconfig(self, hostname, username, password):

        t = paramiko.Transport((hostname, port))

        t.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(t)

        from spidermanager.service.config_generator import generate_config

        local_path = generate_config(self.user)

        print local_path

        sftp.put(local_path, self.config_path)

        print self.config_path

        t.close

    # uploadconfig(hostname, username, password)

    def deleteconfig(self, hostname, username, password):
        command = 'rm -r ' + self.config_path
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command=command)
        print stderr.read()
        print stderr.read()
        print stdout.read()
        ssh.close()

    # deleteconfig(hostname, username, password)

    def prepare(self, hostname, username, password):
        self.mkconfigdir(hostname, username, password)
        self.mklogdir(hostname, username, password)
        self.uploadconfig(hostname, username, password)

    # prepare(hostname, username, password)

    def killallcomponent(self, hostname, username, password):
        command = 'ps -ef |grep ' + self.user +'.json | grep -v grep |awk \'{print $2}\'|xargs kill -s 9'
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command=command)
        print stderr.read()
        print stdout.read()
        ssh.close()

    # killall(hostname, username, password)

    def startwebui(self, hostname, username, password):
        command = 'nohup python ' + engine_pyspider_dir + '/run.py -c ' + self.config_path + ' webui >> '+ self.log_path_master + ' &'
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        #测试环境需要加command0才能启动webui，而生产环境不加才能启动 T.T
        stdin, stdout, stderr = ssh.exec_command(command=command0+command)
        print stderr.read()
        print stdout.read()
        ssh.close()
    
    # startwebui(hostname, username, password)
    
    def startscheduler(self, hostname, username, password):
        command = 'nohup python ' + engine_pyspider_dir + '/run.py -c ' + self.config_path + ' scheduler >> ' + self.log_path_master + ' &'
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command=command0+command)
        print stderr.read()
        print stdout.read()
        ssh.close()
    
    # startscheduler(hostname, username, password)
    
    def startfetcher(self, hostname, username, password, user_type):
        command = 'nohup python ' + engine_pyspider_dir + '/run.py -c ' + self.config_path + ' fetcher >> ' +self.log_path_slave + ' &'
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        if user_type == 'ultimate':
            num_fetcher = 50
        elif user_type == 'premium':
            num_fetcher = 10
        else:
            num_fetcher = 1
        for i in range(1,num_fetcher):
            command=command+command
        stdin, stdout, stderr = ssh.exec_command(command=command0+command)
        print stderr.read()
        print stdout.read()
        ssh.close()
    
    # startfetcher(hostname, username, password)
    
    def startprocessor(self, hostname, username, password):
        command = 'nohup python ' + engine_pyspider_dir + '/run.py -c ' + self.config_path + ' processor >> ' + self.log_path_slave + ' &'
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command=command0+command)
        print stderr.read()
        print stdout.read()
        ssh.close()
    
    # startprocessor(hostname, username, password)
    
    def startresultworker(self, hostname, username, password):
        command = 'nohup python ' + engine_pyspider_dir + '/run.py -c ' + self.config_path + ' result_worker >> ' + self.log_path_slave + ' &'
        print command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command=command0+command)
        print stderr.read()
        print stdout.read()
        ssh.close()

    def startmanagernode(self, hostname, username, password):
        self.prepare(hostname, username, password)
        self.startwebui(hostname, username, password)
        self.startscheduler(hostname, username, password)
    
    def startworkernode(self, hostname, username, password, user_type):
        self.prepare(hostname, username, password)
        self.startfetcher(hostname, username, password, user_type)
        self.startprocessor(hostname, username, password)
        self.startresultworker(hostname, username, password)
    
    def startallmanagernode(self):
        for i in range(0, len(managerhosts)):
            self.startmanagernode(managerhosts[i], username, password)
    
    def startallworkernode(self,user_type):
        for i in range(0, len(workerhosts)):
            self.startworkernode(workerhosts[i], username, password, user_type)
        
    def startall(self,user_type):
        self.startallmanagernode()
        self.startallworkernode(user_type)
    
    def killall(self):
        for i in range(0, len(allhosts)):
            self.killallcomponent(allhosts[i], username, password)
    

# rc = RemoteController("user1")
#
# rc.startall()
# rc.killall()