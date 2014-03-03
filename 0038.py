# -*- coding: utf-8 -*-

_ans = 0
for _i in range(1, 1000000):
    _s = ''
    for _j in range(1, 10):
        _s += str(_i * _j)
        if len(_s) > 9:     break
        if len(_s) == 9:
            if '0' not in _s and len(set(_s)) == 9:
                _ans = max(_ans, int(_s))
print _ans
