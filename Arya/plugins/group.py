# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from Arya.backends.base_module import BaseSaltModule

class Group(BaseSaltModule):
    def uid(self,*args,**kwargs):
        pass
    def gid(self,*args,**kwargs):
        pass
    def present(self,*args,**kwargs):
        pass
    def is_required(self, *args, **kwargs):
        print(args,kwargs)
        name = args[1]
        cmd = '''more /etc/group|awk -F':' '{print $1}'|grep -w %s -q;echo $?'''%name
        return cmd


class UbuntuGroup(Group):
    def home(self,*args,**kwargs):
        print 'in the ubuntu home'