# -*- coding:utf8 -*-

cnt = 2
n = 3
while True:
    n += 1
    if not n % 2 or not n % 3:  continue
    tag = True
    for _ in range(2, (int)(n ** 0.5) + 1):
        if not n % _:
            tag = False
            break
    if tag:                     cnt += 1
    if cnt == 10001:            break
print n
