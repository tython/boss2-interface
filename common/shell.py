#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 1:49
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : shell.py
# @Software: PyCharm


import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        if output:
            output = output.decode("gbk")
        if errors:
            errors = errors.decode("gbk")
        return output,errors

if __name__ == '__main__':
    s = Shell.invoke('dir')