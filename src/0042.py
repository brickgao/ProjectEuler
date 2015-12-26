# -*- coding: utf-8 -*-

_l = []  # Fill in _l
_ans = 0

for _e in _l:
    _total = 0
    for _c in _e:
        _total += ord(_c) - ord('A') + 1
    _total *= 2
    for _i in range(1, 200):
        if _i * (_i + 1) == _total:
            _ans += 1
            break

print _ans
