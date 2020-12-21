#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 23:57
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : login_authentication.py
# @Software: PyCharm

from core.result_base import ResultBase
from api.boss2_api import login
from common.logger import logger


def login_user(username, password):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "email": username,
        "password": password
    }
    header = {
        "Content-Type": "application/json"
    }
    res = login.login_action(json=payload, headers=header)
    print("tyw=>:",res.json())
    result.success = False
    if res.json()["ret_code"] == 0:
        result.success = True
        result.token = res.json()["boss2_sk"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["ret_code"], res.json()["message"])
    result.msg = res.json()["message"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result