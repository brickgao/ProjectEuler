# -*- coding: utf-8 -*-

_sum = 0
for i in range(10, 999999):
    _s = str(i)
    _tmp = 0
    for _ in _s:
        _tmp += int(_) ** 5
    if _tmp == i:
        _sum += i
print _sum
