# !/usr/bin/python
# -*- coding: UTF-8 -*-

print '1000以内的水仙花数为：'
for i in range(100, 1000):
    m = i/100
    n = i/10 % 10
    k = i % 10
    if i == m ** 3 + n ** 3 + k ** 3:
        print i


