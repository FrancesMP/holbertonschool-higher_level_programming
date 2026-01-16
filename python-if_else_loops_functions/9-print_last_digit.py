#!/usr/bin/python3
def print_last_digit(number):
    LD = abs(number) % 10
    print(LD, end="")
    return LD
