# -*- coding: utf-8 -*-

_ans = 0

for _i in range(1, 1001):
    _ans += _i ** _i

print str(_ans)[-10:]
