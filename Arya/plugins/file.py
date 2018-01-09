# -*- coding:utf-8 -*-
from Arya.backends.base_module import BaseSaltModule

class File(BaseSaltModule):

    def is_required(self, *args, **kwargs):
        print('9-9',args,kwargs)
        file_path = args[1]
        cmd = "test -f %s;echo $?"%file_path
        return cmd
