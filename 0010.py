# -*- coding: utf-8 -*-

_is = [True for x in range(2 * 10 ** 6)]
_is[0], _is[1] = False, False
_p = [2]
_e = int((2 * 10 ** 6) ** 0.5) + 1
for i in range(4, 2 * 10 ** 6, 2):
    _is[i] = False
for i in range(3, _e, 2):
    if _is[i]:
        _p.append(i)
        for j in range(i ** 2, 2 * 10 ** 6, i * 2):
            _is[j] = False
for i in range(_e | 1, 2 * 10 ** 6, 2):
    if _is[i]:
        _p.append(i)
ret = 0
for _ in _p:
    ret += _
print ret
    
