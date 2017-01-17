#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

int10 = functools.partial(int, base=10)
print('100 = ', int10('100'))

max2 = functools.partial(max, 10)
print(max2(3, 5, 6))
