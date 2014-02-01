# -*- coding: utf-8 -*-

ret, n, l = 1, 1, 2
_upper = (1001 - 1) / 2
for i in range(_upper):
    ret += n * 4 + 10 * l
    n, l= n + l * 4, l + 2
print ret
    
