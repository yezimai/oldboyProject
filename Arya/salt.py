# -*- coding:utf-8 -*-
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oldboyProject.settings")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print os.path.dirname(os.path.abspath(__file__))
    #print BASE_DIR
    sys.path.append(BASE_DIR)
    from Arya.action_list import actions
    from Arya.backends.utils import ArgvManagement
    #print(sys.argv)
    obj = ArgvManagement(sys.argv)