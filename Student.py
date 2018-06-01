#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: d:\Learn-python\Student.py
# Last Modified: Fri Jun 01 2018
# Modified By: yinchao
###

__author__ = "yinchao"

class Student(object):
    
    counts = 0

    # __slots__ = ("__name", "__score")

    def __init__(self, name, score, addr = "GuangZhou"):  # 初始化方法(也就是构造函数)
        self.__name = name  # 两个下划线代表私有变量，不允许外部修改
        self.__score = score
        self.__addr = addr
        Student.counts = Student.counts + 1

    def __len__(self):
        return 2

    def getGrade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 80:
            return 'B'
        
    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score

    def setName(self, name):
        if type(name) == type("a"):
            self.__name = name

    def setScore(self, score):
        if type(score) == type(1) and score >= 0 and score <= 100:
            self.__score = score

    # useing @property
    @property
    def addr(self):
        return self.__addr

    @addr.setter
    def addr(self, addr):
        if type(addr) == type("abc"):
            self.__addr = addr
    