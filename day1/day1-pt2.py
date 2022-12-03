#!/usr/bin/env python3


with open('input.txt', 'r') as f:
    n = 0
    calorie_list = []
    for i in f.readlines():
        try:
            n += int(i)
        except ValueError:
            calorie_list.append(n)
            n = 0

calorie_list.sort(reverse=True)
total = calorie_list[0] + calorie_list[1] + calorie_list[2]
print(total)