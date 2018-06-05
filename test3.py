#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: d:\Learn-python\test3.py
# Last Modified: Tue Jun 05 2018
# Modified By: yinchao
###

# io编程
# 同步IO
# 文件

###
# f.open()
# f.read(), f.read(size)
# f.close()
###

import io

with open("test2.py", "r", encoding = "utf-8") as f:
    # print(f.read()) # 方法 3

    # while True:   # 方法 2
    #     string = f.readline()
    #     if string == '':
    #         break
    #     print(string)

    # string = f.readlines()  # 方法 1
    # for stri in string:
    #     print(stri)
    
    pass


if __name__ == "__main__":
    pass