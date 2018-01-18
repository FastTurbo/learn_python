# !/usr/bin/python
# -*- coding: UTF-8 -*-

tn = 0
sn = []
n = int(raw_input('n = \n'))
a = int(raw_input('a = \n'))
for count in range(n):
    tn = tn + a
    a = a * 10
    sn.append(tn)
    print tn

sn = reduce(lambda x, y: x + y, sn)
print '计算和为:',sn
