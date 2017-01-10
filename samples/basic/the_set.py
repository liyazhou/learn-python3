#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
s3 = s1 & s2
print(s3)
s4 = s1 | s2
print(s4)
s1.add('5')
print(s1)
s1.add(0.5)
print(s1)
s1.remove(3)
print(s1)
