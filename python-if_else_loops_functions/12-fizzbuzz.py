#!/usr/bin/python3
def fizzbuzz():
    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = "FizzBuzz"
    if number % 5 == 0:
        print("{}".format(buzz))
    elif number % 3 == 0:
        print("{}".format(fizz))
    else number % 5 == 0 and number % 3 == 0:
        print("{}".format(fizzbuzz))
