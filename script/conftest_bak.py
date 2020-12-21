#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 0:19
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : conftest_bak.py
# @Software: PyCharm

import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))
import pytest
import requests
from conf import setting

auth_path = "/auth/login_action/"

json_login = {
   "email": "admin@example.com",
   "password": "zhu88jie"
}

def pytest_addoption(parser):
    parser.addoption("--ip", action="store", default="XX.XX.XX.XX", help="please input target VM ip.")
    parser.addoption("--port", action="store", default="api", help="please input target service port.")

@pytest.fixture(scope="session")
def ip(request):
    if request.config.getoption("--ip") is None:
        return setting.server_ip('testing')
    return request.config.getoption("--ip")

@pytest.fixture(scope="session")
def port(request):
    if request.config.getoption("--port") is None:
        return
    return request.config.getoption("--port")

@pytest.fixture(scope="session")
def uri(ip,port):
    uri = "http://%s/%s" % (ip, port)
    return uri

@pytest.fixture(scope="session")
def auth_token(uri):
    headers = {"User-Agent": "automation",
               "content-type": "application/json;charset=UTF-8"
               }

    post_response = requests.post(url=uri + auth_path,
                                  json=json_login,
                                  headers=headers)
    assert post_response.status_code == requests.status_codes.codes.OK
    resp_payload = post_response.json()
    assert resp_payload['status'] == 200  # to be defined.
    boss2_sk = resp_payload['boss2_sk']
    print("返回的boss2_sk：",boss2_sk)
    return boss2_sk

@pytest.fixture(scope="session")
def headers(uri):
    headers = {"User-Agent": "automation",
               "content-type": "application/json;charset=UTF-8"
               }

    post_response = requests.post(url=uri + auth_path,
                                  json=json_login,
                                  headers=headers)
    assert post_response.status_code == requests.status_codes.codes.OK
    resp_payload = post_response.json()
    assert resp_payload['status'] == 200  # to be defined.
    boss2_sk = resp_payload['boss2_sk']

    headers = {"User-Agent": "automation",
               "content-type": "application/json;charset=UTF-8",
               "T-AUTH-TOKEN": boss2_sk}
    return headers

@pytest.fixture(scope="session")
def cookies(uri):
    headers = {"User-Agent": "automation",
               "content-type": "application/json;charset=UTF-8"
               }

    post_response = requests.post(url=uri + auth_path,
                                  json=json_login,
                                  headers=headers)
    assert post_response.status_code == requests.status_codes.codes.OK
    resp_payload = post_response.json()
    assert resp_payload['status'] == 200  # to be defined.
    boss2_sk = resp_payload['boss2_sk']

    cookies = {"boss2_sk":boss2_sk}
    return cookies












if __name__ == '__main__':
    pytest.main(['-s','-v'])