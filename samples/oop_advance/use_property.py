#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
try:
    s.score = 9999
except ValueError as e:
    print('ValueError: ', e)


class Student2(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._brith = value

    @property
    def age(self):
        return 2015 - self._brith


s = Student2()
s.birth = 1988
print(s.age)
