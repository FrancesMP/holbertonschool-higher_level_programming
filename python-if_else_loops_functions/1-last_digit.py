#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LD = (number % 10) if number >= 0 else -(abs(number) % 10)
if LD > 5:
    print(f"Last digit of {number} is {LD} and is greater than 5")
elif LD == 0:
    print(f"Last digit of {number} is {LD} and is 0")
else:
    print(f"Last digit of {number} is {LD} and is less than 6 and not 0")
