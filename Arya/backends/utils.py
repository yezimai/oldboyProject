# -*- coding:utf-8 -*-
import sys
from Arya.action_list import actions
import django
django.setup()
from Arya import models
from oldboyProject import settings
class ArgvManagement(object):
    def __init__(self,argvs):
        self.sys_argvs =argvs
        self.argv_parse()

    def argv_parse(self):
        #print(self.argvs)
        if len(self.sys_argvs) < 2:
            print 'available module'
            print self.help_msg()
        module_name = self.sys_argvs[1]
        if '.' in module_name:
            mod_name,mod_method = module_name.split('.')
            module_instance = actions.get(mod_name)
            if module_instance:
                module_obj = module_instance(self.sys_argvs,models,settings)
                module_obj.process()
                if hasattr(module_obj,mod_method):
                    mod_method_obj = getattr(module_obj,mod_method)
                    mod_method_obj() #d调用指定的指令执行
                else:
                    exit('module [%s] has not [%s] method'%(mod_name,mod_method))
        else:
            exit('invalid module name argv')


    def help_msg(self):

        for register_module in actions:
            print('\t%s'%register_module)
        exit()