#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))
print(float('1.3'))
print(int('324'))
print(str(342))
print(bool(-1))
print(bool(0))
print(bool(1))
print(bool())
print(bool(''))
print(bool(""))
print(bool("test"))
print(hex(2394))


# print(hex('239874'))


def area_of_circle(circle_r):
    return 3.14 * circle_r * circle_r


x = int(input('input circle r: '))
print(area_of_circle(x))
