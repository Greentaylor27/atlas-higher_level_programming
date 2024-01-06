#!/usr/bin/python3
from calculator_1 import add, sub, mul,div
a = 10
b = 5
if __name__ == "__main__":
    if add(a, b):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sub(a, b):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif mul(a, b):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
