#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())


def lazy_sum2(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f2 = lazy_sum2(1, 2, 4, 5, 7, 8, 9)
print(f2)
print(f2)


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1)
print(f1())
print(f2)
print(f2())
print(f3)
print(f3())


def count2():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


print('count2-----')
print(count2())


def count3():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f())
    return fs


print('count3-----')
print(count3())


# fix:
def count():
    fs = []

    def f(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count3():
    fs = []

    def f(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
