#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        my_list = []
    mul_of_2 = [num for num in my_list if num % 2 == 0]
    return mul_of_2
