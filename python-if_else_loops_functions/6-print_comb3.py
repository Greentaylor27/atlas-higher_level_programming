#!/usr/bin/python3
for tens in range(9):
    for ones in range(tens, 10):
            if tens != ones:
                print("{}{}".format(tens, ones), end=", ")
