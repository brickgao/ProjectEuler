# -*- coding: utf-8 -*-

e1, e2 = 0, 1 
ret = 0
while True:
    _ = e1 + e2
    if _ > 4 * 10**6:   break
    if not _ % 2:       ret += _
    e1, e2 = e2, _
print ret
