# -*- coding: utf-8 -*-

_l1, _l2 = [1], [2]
_l3, _l4 = [3], [2]

_n = 5
while True:
    if len(_l1) == 4 and len(_l2) == 4 and len(_l3) == 4 and len(_l4) == 4:
        print _n - 4
        break
    _l1 = _l2
    _l2 = _l3
    _l3 = _l4
    _tmp = _n
    _l = []
    for _e in range(2, int(_n ** 0.5)):
        if not _tmp % _e:
            _l.append(_e)
            while not _tmp % _e:
                _tmp /= _e
    if _tmp != 1:
        _l.append(_tmp)
    _l4 = _l
    _n += 1
