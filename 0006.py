# -*- coding: utf-8 -*-

_t1, _t2 = 0, 0
for i in range(1, 101):
    _t1 += i * i
    _t2 += i
_t2 = _t2 ** 2
print abs(_t2 - _t1)
