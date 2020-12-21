#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 0:21
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : setting.py
# @Software: PyCharm


import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_PATH,'log','test_log.log')

api_root_url = 'http://boss2.testing.com'
# api_root_url = '192.168.5.200:80'

def server_ip(env):
    if env == "testing":
        server_ip = 'http://boss2.testing.com'
        return server_ip
    elif env == "staging":
        server_ip = 'http://boss2.staging.com'
        return server_ip
    else:
        print("get envorment ip error")