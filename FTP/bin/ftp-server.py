# -*- coding:utf-8 -*-

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE = os.path.dirname(os.path.abspath(__file__))
# print BASE,BASE_DIR
sys.path.append(BASE_DIR)
from modules import main

if __name__ == '__main__':
    Entrypoint = main.ArgvHandler(sys.argv)
    # print("\033[32;1m--client get file --\033[0m")
