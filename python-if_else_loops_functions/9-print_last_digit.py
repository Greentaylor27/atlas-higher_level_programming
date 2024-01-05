#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        new_num = -(abs(number))
    else:
        new_num = abs(number)
    return new_num % 10
