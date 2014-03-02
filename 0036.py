# -*- coding: utf-8 -*-

_ans = 0

for i in range(1, 10 ** 6 + 1):
    _s_ten = str(i)
    _s_bin = bin(i)[2:]
    if _s_ten == _s_ten[::-1] and _s_bin == _s_bin[::-1]:
        _ans += i

print _ans
