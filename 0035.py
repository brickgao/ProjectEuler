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

_ans = 0

for _num in _p:
    _s = str(_num)
    _flag = True
    for i in range(1, len(_s)):
        _tmp = int(_s[i:] + _s[:i])
        if not _is[_tmp]:
            _flag = False
            break
    if _flag:
        _ans += 1

print _ans
