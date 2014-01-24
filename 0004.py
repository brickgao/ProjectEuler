# -*- coding:utf8 -*-

ret = -1
for i in range(100, 1000):
    for j in range(i, 1000):
        _ = i * j
        _s = str(_)
        if _s == _s[::-1]:
            ret = max(ret, i * j)
print ret
