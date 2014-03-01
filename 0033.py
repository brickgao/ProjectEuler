# -*- coding: utf-8 -*-

import fractions

_l_ans = []

for i in range(10, 100):
    for j in range(i + 1, 100):
        _l1 = [str(i)[0], str(i)[1]]
        _l2 = [str(j)[0], str(j)[1]]
        _l1 = map(int, _l1)
        _l2 = map(int, _l2)
        if _l1[0] == _l2[1] and _l2[0] != 0 and float(i) / float(j) == float(_l1[1]) / float(_l2[0]):
            _l_ans.append((i, j))
            break
        if _l1[1] == _l2[0] and _l2[1] != 0 and float(i) / float(j) == float(_l1[0]) / float(_l2[1]):
            _l_ans.append((i, j))

_n1, _n2 = 1, 1
for _ in _l_ans:
    _n1 *= _[0]
    _n2 *= _[1]
print _n2 / fractions.gcd(_n1, _n2)
