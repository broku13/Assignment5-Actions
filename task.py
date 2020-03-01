import math


def firstrun():
    return "success"


def circle_area(radius):
    return math.pi * radius * radius


def first_last(_list):
    return _list[0], _list[len(_list) - 1]


def days_between(day1, day2):
    return day2 - day1
