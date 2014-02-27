# -*- coding: utf-8 -*-

_ans = []
for i in range(1, 100000):
    j = 1
    while True:
        k = i * j
        _length = len(str(i)) + len(str(j)) + len(str(k))
        if _length > 9:     break
        _l = []
        for _ in str(i):  _l.append(_)
        for _ in str(j):  _l.append(_)
        for _ in str(k):  _l.append(_)
        if '0' not in _l and len(_l) == 9 and len(set(_l)) == 9:
            _ans.append(k)
        j += 1
ret = 0
_ans = set(_ans)
for _ in _ans:      ret += _
print ret
