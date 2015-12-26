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
for i in range(3, 10 ** 6 + 1, 2):
    if _is[i]:
        _p.append(i)

_begin = -1
for _i in range(0, len(_p)):
    if len(str(_p[_i])) == 4:
        _begin = _i
        break
for _i in range(_begin, len(_p)):
    if len(str(_p[_i])) > 4:
        _end = _i
        break

for _i in range(_begin, _end):
    for _j in range(_i + 1, _end):
        if _is[2 * _p[_j] - _p[_i]]:
            _l1, _l2, _l3 = (
                list(str(_p[_i])),
                list(str(_p[_j])),
                list(str(2 * _p[_j] - _p[_i]))
            )
            _l1.sort()
            _l2.sort()
            _l3.sort()
            if _l1 == _l2 and _l2 == _l3:
                print str(_p[_i]) + str(_p[_j]) + str(2 * _p[_j] - _p[_i])
