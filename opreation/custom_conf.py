#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 0:45
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : custom_conf.py
# @Software: PyCharm


from core.result_base import ResultBase
from api.boss2_api import custom_conf
from common.logger import logger


def get_custom_conf(function,key):
    """
    读取配置(Boss2GetCustomConf)
    :param function:功能名称
    :param key:key 字符串，由"."分隔的字符串，如果要读取功能的整个配置，不要传 key 参数。
    :return:
    """
    result = ResultBase()
    res = custom_conf.get_custom_conf(function,key)
    result.success = False
    if res.json()["ret_code"] == 0:
        result.success = True
    else:
        result.error = "查询用户 ==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["ret_code"], res.json())
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("查看单个用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result