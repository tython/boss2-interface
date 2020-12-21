#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 1:36
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : http_requests.py
# @Software: PyCharm

import requests
import logging


class HttpRequest:

    def get(self, url, params, **kwargs):
        try:
            res = requests.get(url, params=params, **kwargs)
        except (TimeoutError,Exception) as e:
            logging.error('get 请求失败',e)
        else:
            return res

    def post(self, url, data=None, json=None, **kwargs):
        try:
            res = requests.post(url, data=data, json=json, **kwargs)
        except (TimeoutError, Exception) as e:
            logging.error('post 请求失败', e)
        else:
            return res

    def vist_req(self, method, url, params=None, data=None, json=None, **kwargs):
        if method.lower == 'get':
            return self.get(url, params=params, **kwargs)
        elif method.lower == 'post':
            return self.post(url, data=data, json=json, params=params, **kwargs)
        else:
            return requests.request(method, url, **kwargs)

    def http_request(self, method, url, params=None, data=None, json=None, **kwargs):
        res = self.vist_req(method,url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except:
            logging.error('不是json格式的数据')