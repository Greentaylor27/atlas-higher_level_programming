#!/usr/bin/python3
def fizzbuzz():
    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = "FizzBuzz"
    number = 100
    while number < 100:
        print(number)
        if number % 5 == 0:
            print("{Buzz}")
        elif number % 3 == 0:
            print("{Fizz}")
        elif number % 5 == 0 and number % 3 == 0:
            print("{FizzBuzz}")
