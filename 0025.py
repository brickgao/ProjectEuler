# -*- coding: utf-8 -*-

_r1, _r2, _term = 1, 1, 3
while True:
    _tmp = _r1 + _r2
    if len(str(_tmp)) >= 1000:
        print _term
        break
    _term += 1
    _r1, _r2 = _r2, _tmp
