#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: d:\Learn-python\module.py
# Last Modified: Thu May 31 2018
# Modified By: yinchao
###

"""
    在python中，仅仅也是用名称区别公有变量和私有变量，并没有特别的机制能
    严格控制不能访问模块中的私有变量.
"""

__author__ = 'yinchao'

import sys

# 私有变量， 在变量前加一个 _
def _printTheAuthor():
    print(__author__)

# 公有变量， 不用加。。。
def printTheAuthor():
    print(__author__)

# 特殊变量, __name__ 或者 __author__ 等等
if __name__ == "__main__":
    _printTheAuthor()