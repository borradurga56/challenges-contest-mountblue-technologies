#!/usr/bin/env python
t = int(input().strip())
rem = 3
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)
