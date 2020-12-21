#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 0:08
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : conftest.py
# @Software: PyCharm

import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))
import pytest
import allure
from api.boss2_api import login
from common.read_data import data
from common.logger import logger


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data

login_data = get_data("api_test_login_data.yml")
print(login_data)

@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")

@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, password):
    logger.info("前置步骤 ==>> 管理员:{} 登录，密码为：{}".format(username, password))

@pytest.fixture(scope="session")
def login_fixture():
    email = login_data["test_login_user"]["email"]
    password = login_data["test_login_user"]["password"]
    header = {
        "Content-Type": "application/json"
    }
    payload = {
        "email": email,
        "password": password,
    }
    loginInfo = login.login_action(json=payload, headers=header)
    step_login(email, password)
    yield loginInfo.json()


