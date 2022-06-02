#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    print(a, "+", b, "=", add(a, b))
    print(a, "-", b, "=", sub(a, b))
    print(a, "*", b, "=", mul(a, b))
    print(a, "/", b, "=", div(a, b))
