# -*- coding:utf -*-

ret = 0
_mn = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_mr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_d = (366 + 0) % 7
for i in range(1901, 2001):
    if not i % 4 and not i % 400:   _ = _mn
    else:                           _ = _mr
    for j in range(1, 13):
        if _d == 6:     ret += 1
        _d = (_[j] + _d) % 7
print ret
