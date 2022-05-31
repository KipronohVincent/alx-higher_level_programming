#!/usr/bin/python3


def fizzbuzz():
    for m in range(1, 101):
        if m % 3 == 0 and m % 5 == 0:
            print("FizzBuzz ", end="")
        elif m % 3 == 0:
            print("Fizz ", end="")
        elif m % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(m), end="")
