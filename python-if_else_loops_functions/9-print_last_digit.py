#!/usr/bin/python3
def print_last_digit(number):
    new_num = abs(number) % 10
    print(new_num, end="")
    return new_num
