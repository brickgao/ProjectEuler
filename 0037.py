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

_total = 0
_ans = 0
for _e in _p[4:]:
    _s = str(_e)
    _flag = True
    for _i in range(1, len(str(_s))):
        _num = int(_s[_i:])
        if not _is[_num]:
            _flag = False
            break
        _num = int(_s[:_i])
        if not _is[_num]:
            _flag = False
            break
    if _flag:
        _total += 1
        _ans += _e
    if _total == 11:
        break
print _ans
