#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
print([k for k in d])
print([v for v in d.values()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

testList = ['Hello', 'World', 'IBM', 18, 'Apple']
print(testList)
print([s.lower() for s in testList if isinstance(s, str)])
