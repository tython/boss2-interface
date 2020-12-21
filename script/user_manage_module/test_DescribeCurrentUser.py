#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 1:44
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : test_DescribeCurrentUser.py
# @Software: PyCharm


import pytest
import allure
from opreation.user_manage import describecurrentuser
# from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 根据ID修改用户信息")
def step_1(id):
    logger.info("步骤1 ==>> 修改用户ID：{}".format(id))


@allure.step("前置登录步骤 ==>> 管理员登录")
def step_login(admin_user, token):
    logger.info("前置登录步骤 ==>> 管理员 {} 登录 ==>> 返回的 token 为：{}".format(admin_user, token))

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("用户管理")
@allure.feature("获取当前用户信息")
class TestUserManage():
    """获取用户信息"""

    @allure.story("用例--获取用户信息")
    @allure.description("该用例是测试：获取用户信息")
    @pytest.mark.custom_conf
    @pytest.mark.usefixtures("login_fixture")
    def test_DescribeCurrentUser(self, login_fixture):
        logger.info("*************** 开始执行用例 ***************")
        user_login_info = login_fixture
        print("user_login_info:",user_login_info)
        admin_user = user_login_info.get("username")
        email = user_login_info.get("email")
        token = user_login_info.get("boss2_sk")
        step_login(admin_user, token)
        result = describecurrentuser(token)
        print("result:",result)
        logger.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_DescribeCurrentUser.py"])