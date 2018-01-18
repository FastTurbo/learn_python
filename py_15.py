# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 一般定义函数def x(x)，上下应该空出两个空白行出来


def k(x):
    if x in range(60):
        print('D')
    elif x in range(60,90):
        print('B')
    else:
        print('A')


score = int(raw_input('输入分数：\n'))
k(score)


