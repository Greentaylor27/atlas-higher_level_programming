#!/usr/bin/python3
i = 97
for i in range(97, 123):
    char = chr(i)
    if char != 'e' and char != 'q':
        print("{}".format(char), end="")
