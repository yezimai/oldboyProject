# -*- coding:utf-8 -*-
from Arya.backends.base_module import BaseSaltModule

class Pkg(BaseSaltModule):
    def is_required(self, *args, **kwargs):
        print(args,kwargs)