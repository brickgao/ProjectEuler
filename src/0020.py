# -*- coding: utf-8 -*-


def fac(n):
    return not n and 1 or n * fac(n - 1)


_s = str(fac(100))
ret = 0
for _ in _s:
    ret += int(_)
print ret
