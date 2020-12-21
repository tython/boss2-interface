#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 1:40
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : user_manage.py
# @Software: PyCharm


from core.result_base import ResultBase
from api.boss2_api import user_manage
from common.logger import logger


def describecurrentuser(token=None):
    result = ResultBase()
    headers = {
        "Content-Type": "application/json"
    }
    cookies = {
        "boss2_sk":token
    }
    payload = {
        "action": "Boss2DescribeCurrentUser"
    }
    res = user_manage.describecurrentuser(json=payload,headers=headers,cookies=cookies)
    result.success = False
    if res.json()["ret_code"] == 0:
        result.success = True
    else:
        result.error = "查询用户 ==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["ret_code"], res.json())
    result.msg = res.json()["action"]
    result.response = res
    logger.info("查看单个用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

