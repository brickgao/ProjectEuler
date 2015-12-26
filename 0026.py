# -*- coding: utf-8 -*-

from decimal import *

ret1, ret2 = 0, 0
getcontext().prec = 3000
for i in range(2, 1000):
    _s = str(Decimal(1) / Decimal(i))
    if len(_s) < 3002:
        continue
    _s = _s[::-1][1:]
    for j in range(1, i):
        if _s[:j] == _s[j:2 * j]:
            if j > ret2:
                ret1, ret2 = i, j
            break
print ret1
