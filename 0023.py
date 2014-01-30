# -*- coding: utf-8 -*-

_arr = []
_is = [0 for i in range(30000)]
for i in range(2, 28124):
    _sum = 0
    _upper = int(i ** 0.5) + 1
    _r = []
    for j in range(1, _upper + 1):
        if not i % j:   _r += [j, i / j]
    _r = set(_r)
    for j in _r:
        if j != i:      _sum += j
    if _sum > i:
        _arr.append(i)
_len = len(_arr)
for i in range(_len):
    for j in range(i, _len):
        _tmp = _arr[i] + _arr[j]
        if _tmp < 30000:
            _is[_tmp] = 1
ret = 0
for i in range(28124):
    if not _is[i]:
        ret += i
print ret
