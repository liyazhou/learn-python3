#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def nop():
    pass


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

print(math.sqrt(4))

# TypeError: bad operand type:
my_abs('123')
# #
# import math
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# print(my_abs(-20))
# x, y = move(100, 20, 60, math.pi / 6)
# print(x, y)
#
# print(my_abs('sdjfl'))
