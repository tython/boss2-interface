#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 15:33
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : http_requests_bak.py
# @Software: PyCharm

import requests
from common.logger_bak import logger
from requests.auth import HTTPBasicAuth
from conf.setting import *
from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    from requests.packages import urllib3
    urllib3.disable_warnings()
except:
    import logging
    logging.captureWarnings(True)

class HttpRequests:

    @staticmethod
    def http_requests(method=None,url=None,params=None,data=None,json=None,headers=None,files=None,cookies=None,verify=False,cert=None,proxies=None,timeout=30,auth=None):
        """
       :param method:请求的方式，get、post等等
       :param url: 请求的地址 http://xxxx:post
       :param data:传递的参数
       :param headers:传递的请求头
       :param files:上传的文件,例如files={'file':open('favicon.ico','rb')},传二进制文件
       :param cookie:请求时传递的cookie值
       :param verify:是否忽略SSLError,False为忽略，True为显示
       :param cert:指定证书文件，需要有crt和key文件，并且指定他们的路径,例如cert=('/path/server.crt','/path/key')
       :param proxies:设置代理,例如proies = {"http":"http://10.10.1.10:3128","https":"http://10.10.1.10:1080"}
       :param timeout:设置请求的超时时间,连接和读取的总时长,例如timeout=1
       :param auth:用户认证，auth=HTTPBasicAuth('username','password')
       :return:
        """
        try:
            if method.strip().lower() == 'get' or method == None:
                res = requests.get(url=url,params=params,headers=headers,cookies=cookies,verify=verify,cert=cert,proxies=proxies,timeout=timeout,auth=auth)
            elif method.strip().lower() == 'post':
                res = requests.post(url=url,data=data,json=json,headers=headers,cookies=cookies,files=files,verify=verify,cert=cert,proxies=proxies,timeout=timeout,auth=auth)
            else:
                logger.error("Unsupported requests")
                raise Exception("Unsupported requests")
            return res
        except ReadTimeout as e:
            logger.exception("time out,{0}".format(e))
            pass
        except HTTPError as e:
            logger.exception("http error,{0}".format(e))
            pass
        except RequestException as e:
            logger.exception("requests error,{0}".format(e))
            pass
        except Exception as e:
            logger.exception("other error,{0}".format(e))
            pass


if __name__ == '__main__':
    url = "http://www.baidu.com"
    res = HttpRequests.http_requests('get',url)
    print(res.text)