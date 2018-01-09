# -*- coding:utf-8 -*-
import SocketServer
import os,sys,hashlib,time
from conf import settings
class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                print self.client_address
                break
            self.instruction_allowcation(data)  #客户端发过来的数据交给这个数据处理
    def instruction_allowcation(self,instructions):
        instructions = instructions.split('|')
        function_str = instructions[0]
        if hasattr(self,function_str):
            func = getattr(self,function_str)
            func(instructions)
        else:
            print('received invalid %s'%instructions)
    def file_get(self,user_data):
        print("\033[32;1m--client get file --\033[0m")
        if self.login_user:
            filename_with_path = json.loads(user_data[1])
            file_abs_path = "%s/%s/%s"%(settings.USER_HOME,self.login_user,filename_with_path)
            print file_abs_path
            if os.path.isfile(file_abs_path):
                file_size = os.path.getsize(file_abs_path)
                response_msg = 'reponse|300|%s|n/a'%(file_size)
                self.request.send(response_msg)
                client_response = self.request.recv(1024).split('|')
                print '---',
                if client_response[1] == "301":
                    sent_size = 0
                    f = open(file_abs_path,'rb')
                    file_md5 = hashlib.md5()
                    t_start = time.time()
                    while file_size != sent_size:
                        data = f.read(4096)
                        self.request.send(data)
                        sent_size += len(data)
                        print("send",file_size,sent_size)
                    else:
                        t_cost = time.time() - t_start
                        print('file transfer time',t_cost)
                        print('success sent')
                        f.close()

            else:
                # response_msg = "reponse|302|n/a|n/a"
                # self.request.send(response_msg)
                print('file do not exist')

    def user_auth(self,data):
        auth_info = json.loads(data[1])
        if auth_info['username'] in settings.USER_ACCOUNT:
            if settings.USER_ACCOUNT[auth_info['username']]['password'] == auth_info['password']:
                response_code = '200'
                self.login_user = auth_info['username']

            else:
                response_code = '201'
        else:
            response_code='202'