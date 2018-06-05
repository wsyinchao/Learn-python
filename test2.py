#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: d:\Learn-python\test2.py
# Last Modified: Mon Jun 04 2018
# Modified By: yinchao
###

# python 代码的错误和调试

import logging
logging.basicConfig(level = logging.DEBUG, 
                    filename = 'log.log',
                    filemode = 'w',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

__author__ = "yc"

# using try except finally 语句

try:
    print("try")
    r = 10 / 0
    print("result..", r)
except BaseException as e:
    print("except..", e)
finally:
    print("finally")
print("END")


s = '0'
n = int(s)
logging.debug('n = %d' % n)
logging.info('n = %d' % n)
logging.error('n = %d' % n)
logging.warning('n = %d' % n)
print(10 / n)

if __name__ == "__main__":
    pass