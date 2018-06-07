#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: d:\Learn-python\test3.py
# Last Modified: Thu Jun 07 2018
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

import os
import io
from io import StringIO
from io import BytesIO

# file IO
with open("test2.py", "r", encoding = "utf-8") as f: # 自动调用 f.close 方法关闭文件流
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

# file-like object
# 在python中返回有read()方法的对象 都被称作file-like object
# 打开二进制文件
# r, rb, w, wb(打开文件的几种方式)
with open("C:/Users/yinchao/Pictures/Saved Pictures/true.jpg", "rb") as f:
    pass


# string IO
# 读取内存或者网络，需要操作字符串流，或者字节流
f = StringIO()
len = f.write("wsyinchao")   # 创建字符流之后可以向文件流那样操作字符流了
print(len)

# 字节流
# 操作二进制数据
f = BytesIO()
f.write("尹超".encode("utf-8"))  # 以字节流写入数据
print(f.getvalue())  #有了流之后，也是想操作文件流那样操作字节流

# 再次记忆
###
# python 在内存中使用 unicode 编码
# "str".encode("encodeType") 转化成字节流,指定编码格式
# b'str'.decode("encodeType") 转化成字符流，指定编码格式
###

# 操作文件和目录
# 查看环境变量
print(os.environ)
# 查看某一个
print(os.environ.get('PATH'))

## 操作目录和文件的函数放在os模块中，和os.path模块中
# 查看当前目录的绝对路径
print(os.path.abspath('.'))

## 在某个目录下创建一个新目录(为了保证跨平台，需要借助python生成正确的路径格式)
# 创建目录
# os.mkdir(os.path.join('.', 'test.test'))

# 删除目录
# os.rmdir(os.path.join('.', 'test.test'))

# os.path.join 合成路径
# os.path.split() 拆分路径, 返回两个字符串，后一个总是最后一级的目录或者文件
# os.path.splitext() 拆分路径，返回两个字符串,后一个是文件后缀名( 该方法就是用来得到文件后缀名的 )

# os.rename() # 重命名
# os.remove() # 删除

if __name__ == "__main__":
    pass