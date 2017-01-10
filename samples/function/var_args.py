#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def person2(name, age, *, city, job):
    print('name: ', name, 'age: ', age, 'city: ', city, 'job:', job)


person2('2', 18, city='tj', job=18)


# person2('2', 18)




def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)


person('lyz', 20)
person('dd', 30, city='rb', whoami='dldsjf')
extra = {'lyz': 18, 'yyy': 20}
person('lyz', 20, **extra)


def calsum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


print(calsum(1, 2, 3))
digs = [1, 3, 5]
print(calsum(*digs))


def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


print(add_end())
print(add_end())
names = ['test', 'lyz']
print(add_end(names))


def enroll(name, age, city='beijing'):
    print('name: ', name)
    print('age: ', age)
    print('city: ', city)


enroll('lyz', 18)
enroll('bj', 16, 'tianjin')


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(10))
print(power(10, 2))


def hello(greeting, *args):
    if (len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))


hello('Hi')  # => greeting='Hi', args=()
hello('Hi', 'Sarah')  # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')  # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names)  # => greeting='Hello', args=('Bart', 'Lisa')
