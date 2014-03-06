# -*- coding: utf-8 -*-

from itertools import permutations

_ans = 0

for _e in permutations('0123456789', 10):
    _s = ''.join(_e)
    if _s[0] == '0':        continue
    if int(_s[1:4]) % 2:    continue
    if int(_s[2:5]) % 3:    continue
    if int(_s[3:6]) % 5:    continue
    if int(_s[4:7]) % 7:    continue
    if int(_s[5:8]) % 11:   continue
    if int(_s[6:9]) % 13:   continue
    if int(_s[7:10]) % 17:  continue
    _ans += int(_s)

print _ans
