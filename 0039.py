# -*- coding: utf-8 -*-

_ans1, _ans2 = 0, 0

for _p in range(3, 1001):
    _l = []
    for _c in range(1, _p):
        _delta = 4 * (_p - _c) ** 2 - 8 * ((_p - _c) ** 2 - _c ** 2)
        if _delta < 0:                          continue
        if int(_delta ** 0.5) ** 2 != _delta:   continue
        _delta_sqrt = int(_delta ** 0.5)
        if _delta_sqrt + 2 * (_p - _c) > 0 and not (_delta_sqrt + 2 * (_p - _c)) % 4:
            _a = (_delta_sqrt + 2 * (_p - _c)) / 4
            _b = _p - _a - _c
            if _a > 0 and _b > 0 and _c > 0:
                if _a > _b:     _a, _b = _b, _a
                _l.append((_a, _b, _c))
        if - _delta_sqrt + 2 * (_p - _c) > 0 and not (- _delta_sqrt + 2 * (_p - _c)) % 4:
            _a = (- _delta_sqrt + 2 * (_p - _c)) / 4
            _b = _p - _a - _c
            if _a > 0 and _b > 0 and _c > 0:
                if _a > _b:     _a, _b = _b, _a
                _l.append((_a, _b, _c))
    _l = set(_l)
    if len(_l) > _ans1:
        _ans1, _ans2 = len(_l), _p

print _ans2
