# -*- coding: utf-8 -*-


mp = []  # Fill in mp
ret = 0
for i in range(20):
    for j in range(20 - 4):
        _t1, _t2 = 1, 1
        for k in range(4):
            _t1 *= mp[i][j + k]
            _t2 *= mp[j + k][i]
        ret = max(_t1, _t2, ret)
for i in range(20 - 4):
    for j in range(20 - 4):
        _t = 1
        for k in range(4):
            _t *= mp[i + k][j + k]
        ret = max(_t, ret)
for i in range(4, 20):
    for j in range(20 - 4):
        _t = 1
        for k in range(4):
            _t *= mp[i - k][j + k]
        ret = max(_t, ret)
print ret
