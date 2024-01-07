#!/usr/bin/python3
import sys as s
if __name__ == "__main__":
    sum = 0
    for arg in s.argv[1:]:
        sum += int(arg)
    print(sum)
