#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))


class Fruit(object):
    def run(self):
        print('Animal is running...')


class Apple(Fruit):
    def run(self):
        print('apple is running')


class Banana(Fruit):
    def run(self):
        print('banana is running')


def run_2(fruit):
    fruit.run()
    fruit.run()


run_2(Apple())
run_2(Banana())
