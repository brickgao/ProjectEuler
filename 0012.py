# -*- coding:utf8 -*-

_n = 1
while True:
    _s, _t = 1, _n * (_n + 1) / 2
    _tt = _t
    for i in range(2, int(_tt ** 0.5 + 1)):
        if not _tt % i:
            _ = 0
            while not _tt % i:
                _tt /= i
                _ += 1
            _s *= _ + 1
    if _s >= 500:   break
    _n += 1
print _t
    
