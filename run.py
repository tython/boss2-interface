#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 1:53
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : run.py
# @Software: PyCharm

import os
import sys
import time
import pytest
from common import shell
from common.logger_bak import logger


import pytest
import pytest



if __name__ == '__main__':
    pytest.main()





# if __name__ == "__main__":
#     file = os.path.basename(sys.argv[0])
#     print(file)
#     # log = logger(file)
#
#     try:
#         print("开始执行脚本")
#         logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "===================================")
#         print("脚本执行完成")
#     except Exception as e:
#         logger.error("脚本批量执行失败！", e)
#         print("脚本批量执行失败！", e)

    # try:
    #     shell = shell.Shell()
    #     cmd = 'allure generate %s -o %s --clean' % ('./report/reportallure/', './report//reporthtml/')
    #     # logger.info("开始执行报告生成")
    #     print("开始执行报告生成")
    #     shell.invoke(cmd)
    #     # logger.info("报告生成完毕")
    #     print("报告生成完毕")
    # except Exception as e:
    #     print("报告生成失败，请重新执行", e)
    #     # logger.error("报告生成失败，请重新执行", e)
    #     # log.error('执行用例失败，请检查环境配置')
    #     raise
    #
    # time.sleep(5)
    # mail()