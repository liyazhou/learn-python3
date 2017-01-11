#!/usr/bin/env python3
# -*- coding: utf-8 -*-


l = [x * x for x in range(5)]
print(l)
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
g = fib(10)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as ex:
        print(ex.args)
        print('value: ', ex.value)
        break
print('--------fib3---------')


def fib3(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


f = fib3(10)
print(f)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
