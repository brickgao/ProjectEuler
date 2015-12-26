# -*- coding: utf-8 -*-

from itertools import permutations
from math import sqrt

_ans = 7
_l = []

for _e in permutations('1234567', 7):
    _num = int(''.join(_e))
    _l.append(_num)

for _num in _l[::-1]:
        _num_sqrt = int(sqrt(_num + 1.0) + 1.0)
        _flag = True
        for _i in range(2, _num_sqrt):
            if not _num % _i:
                _flag = False
                break
        if _flag:
            _ans = max(_ans, _num)
            break

print _ans
