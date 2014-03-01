# -*- coding: utf-8 -*-

_ans = 0

for i in range(3, 241920):
    _l = map(int, str(i))
    _sum = 0
    for _e in _l:   
        if _e != 0:
            _sum += reduce(lambda x, y: x * y, range(1, _e + 1))
        else:
            _sum += 1
    if _sum == i:   _ans += i

print _ans
