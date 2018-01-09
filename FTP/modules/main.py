# -*- coding:utf-8 -*-
import sys

class ArgvHandler(object):
    def __init__(self,args):
        self.args =args
        self.argv_parser()

    def argv_parser(self):
        if len(self.args) < 2:
            self.help()
        else:
            first_argv =self.args[1]
            if hasattr(self,first_argv):
                func=getattr(self,first_argv)
                func()
            else:
                self.help()

    def help(self):
        msg='''
            start:start ftp server
            stop: stop ftp server
            '''
        print msg
    def start(self):
        try:
            server = threading_socket_server.SocketServer.ThreadingTCPServer((setting.BIND_HOST,settings.BIND_PORT),Threading_socket_server.MyTCPHandler)
            server.serve_forever()
        except KeyboardInterrupt:
            print('---going to shut down ftp server')
            server.shutdown()