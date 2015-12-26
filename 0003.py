# -*- coding: utf-8 -*-

n = 600851475143
_ = 2
while True:
    while not n % _:
        n /= _
    if n == 1:
        break
    _ += 1
print _
