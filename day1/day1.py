#!/usr/bin/env python3


with open('input.txt', 'r') as f:
    n = 0
    high = 0
    for i in f.readlines():
        try:
            n += int(i)
        except ValueError:
            if n > high:
                high = n
            n = 0

print(high)