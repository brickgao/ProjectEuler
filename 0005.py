# -*- coding:utf8 -*-

def gcd(a, b):
    if a == 0 and b == 0:   return -1
    if a == 0 or b == 0:    return a | b
    if a > b:   a, b = b, a
    while not a == 0 and not b == 0:
        _ = a % b
        a, b = b, _
    return a | b

ret = 1
for i in xrange(2, 20):
    _t = gcd(ret, i)
    ret = ret * i / _t
print ret

