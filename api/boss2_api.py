#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 23:16
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : boss2_api.py
# @Software: PyCharm

from conf.setting import api_root_url
from core.rest_client import RestClient


class Login_Authentication(RestClient):

    def __init__(self,api_root_url,**kwargs):
        super(Login_Authentication, self).__init__(api_root_url,**kwargs)

    def login_action(self,**kwargs):
        return self.post("/auth/login_action/",**kwargs)

class User_Manage(RestClient):

    def __init__(self,api_root_url,**kwargs):
        super(User_Manage, self).__init__(api_root_url,**kwargs)

    def describecurrentuser(self,**kwargs):
        return self.post("/api/",**kwargs)

class Custom_Conf(RestClient):

    def __init__(self,api_root_url,**kwargs):
        super(Custom_Conf, self).__init__(api_root_url,**kwargs)

    def set_custom_conf(self,**kwargs):
        return self.post("/api/?action=Boss2SetCustomConf",**kwargs)

    def get_custom_conf(self,**kwargs):
        return self.post("/api/?action=Boss2GetCustomConf",**kwargs)


login = Login_Authentication(api_root_url)
user_manage = User_Manage(api_root_url)
custom_conf = Custom_Conf(api_root_url)