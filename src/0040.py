# -*- coding: utf-8 -*-

_ans, _total, _now = 1, 0, 1
_l = [1, 10, 100, 1000, 10000, 100000, 1000000]
while True:
    _s = str(_now)
    for _e in _l:
        if _total < _e and _total + len(_s) >= _e:
            _ans *= int(_s[_e - _total - 1])
    if _total + _now > 10 ** 6:
        break
    _total += len(_s)
    _now += 1
print _ans
