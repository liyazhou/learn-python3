#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
print('______________')

print(d.get('test'))
print(d.get('t', -1))
print(d)
print(d.pop('Bob'))
print(d)
d['t'] = 'liyazhou'
print(d)
d.popitem()
print(d)
d.popitem()
print(d)
d.clear()
print(d)
d = {
    't': 95,
    'a': 75,
    'c': 85
}
print(d)
a = d.copy()
print(a)
