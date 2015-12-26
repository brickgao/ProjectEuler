# -*- coding: utf-8 -*-

_s = str((lambda n: not n and 1 or n * fac(n - 1))(100))
ret = 0
for _ in _s:
    ret += int(_)
print ret
