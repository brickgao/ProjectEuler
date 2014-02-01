# -*- coding: utf-8 -*-

_is = [True for x in range(3 * 10 ** 6)]
_is[0], _is[1] = False, False
_p = [2]
_e = int((3 * 10 ** 6) ** 0.5) + 1
for i in range(4, 3 * 10 ** 6, 2):
    _is[i] = False
for i in range(3, _e, 2):
    if _is[i]:
        _p.append(i)
        for j in range(i ** 2, 3 * 10 ** 6, i * 2):
            _is[j] = False
for i in range(_e | 1, 3 * 10 ** 6, 2):
    if _is[i]:
        _p.append(i)
ret1, ret2 = 0, 0
_index = _p.index(997)
for b in _p[:_index + 1]:
    for a in range(- b + 1, 1000):
        if not _is[a + b + 1]:
            continue
        else:
            n = 2
            while True:
                _ = n * n + a * n + b
                if not _is[_]:
                    break
                n += 1
            if ret1 < n:
                ret1, ret2 = n, a * b
print ret2
