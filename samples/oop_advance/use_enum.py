#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


@unique
class Week(Enum):
    Sun = 0
    Mon = 1
    Tue = 2


day0 = Weekday.Sun
day1 = Weekday.Mon
day2 = Weekday.Tue
day2value = Weekday.Tue.value
print(day2value)
day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)
    # print(name, '=>', member, ',', member.value)

for name, member in Week.__members__.items():
    print(name, '=>', member)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

AbcEnum = Enum('abc', ('a', 'b', 'c'))
for name, member in AbcEnum.__members__.items():
    print(name, '=>', member, ',', member.value)

a = AbcEnum.a
print(a)
print(a.value)
