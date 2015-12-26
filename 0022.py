# -*- coding: utf-8 -*-

ret = 0
arr = []  # Fill in arr
arr.sort()
for i in range(len(arr)):
    _sum = 0
    for _ in arr[i]:
        _sum += ord(_) - ord('A') + 1
    ret += _sum * (i + 1)
print ret
