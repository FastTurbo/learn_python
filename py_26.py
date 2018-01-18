# !/usr/bin/python
# -*- coding: UTF-8 -*-


def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum


n = int(raw_input('输入数字：'))
print '数字%d的阶乘为：%d' % (n, fact(n))
