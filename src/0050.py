# -*- coding: utf-8 -*-

_is = [True for x in range(10 ** 6 + 1)]
_is[0], _is[1] = False, False
_p = [2]
_e = int((10 ** 6 + 1) ** 0.5) + 1
for i in range(4, 10 ** 6 + 1, 2):
    _is[i] = False
for i in range(3, _e, 2):
    if _is[i]:
        for j in range(i ** 2, 10 ** 6, i * 2):
            _is[j] = False

_sum = 0
_p = [0]
for i in range(10 ** 6 + 1):
    if _is[i]:
        _sum += i
        _p.append(_sum)

_ans1, _ans2 = 0, 0
for _i in range(len(_p)):
    for _j in range(_i - _ans1):
        if _p[_i] - _p[_j] >= 1000000:
            break
        if _is[_p[_i] - _p[_j]] and _i - _j > _ans1:
            _ans1, _ans2 = _i - _j, _p[_i] - _p[_j]

print _ans2
