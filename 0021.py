# -*- coding: utf-8 -*-

arr = [0 for x in range(30000)]
ret = 0
for i in range(2, 10000):
    _sum = 0
    for j in range(1, i):
        if not i % j:
            _sum += j
    arr[i] = _sum
for i in range(10000):
    if arr[i] and arr[i] > i and arr[arr[i]] == i:
        ret += arr[i] + i
print ret
    
