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

_n = 33
while True:
    if _n % 2 and not _is[_n]:
        _flag = False
        for _e in _p:
            _tmp = (_n - _e) / 2
            if _tmp <= 0:
                break
            if int(float(_tmp) ** 0.5) ** 2 == _tmp:
                _flag = True
                break
        if not _flag:
            print _n
            break
    _n += 1
