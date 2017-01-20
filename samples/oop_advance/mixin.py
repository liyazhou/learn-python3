#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


class Parrot(Bird):
    pass


class Runnable(object):
    def run(self):
        print('running......')


class Flyable(object):
    def fly(self):
        print('flying......')


class Dog2(Mammal, Runnable):
    pass


class Parrot(Bird, Flyable):
    pass
