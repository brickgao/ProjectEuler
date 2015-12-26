# -*- coding: utf-8 -*-


def is_pentagon(_num):
    _num = _num * 24 + 1
    if int(float(_num) ** 0.5) ** 2 != _num:
        return False
    _num = int(float(_num) ** 0.5) + 1
    if _num % 6:
        return False
    else:
        return True


_l = []
_ans = 99999999999

for _i in range(1, 3000):
    _l.append(_i * (3 * _i - 1) / 2)

_len = len(_l)

for _i in range(_len):
    for _j in range(_i + 1, _len):
        if is_pentagon(_l[_i] + _l[_j]) and is_pentagon(_l[_j] - _l[_i]):
            _ans = min(_ans, _l[_j] - _l[_i])

print _ans
