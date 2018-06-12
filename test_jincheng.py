#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: d:\Learn-python\test_jincheng.py
# Last Modified: Tue Jun 12 2018
# Modified By: yinchao
###

# 多进程 ## 需要了解操作系统相关知识
# 在unix/linux中，使用fork()产生子进程(推荐使用linux学习python)
# 编写多进程服务,linux无疑是正确的选择



# multiprocessing 一个跨平台支持的多进程支持模块
from multiprocessing import Process
import os


# 子进程要执行的代码 ##有待进一步学习
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == "__main__":
    print('Parent process %s' % os.getpid())
    p =  Process(target=run_proc, args=('test',))
    p.start()
    p.join()
    print('child process end')
