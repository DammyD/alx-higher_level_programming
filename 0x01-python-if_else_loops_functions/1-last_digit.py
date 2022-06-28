#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

l_digit = abs(number) % 10
str = f"Last digit of {number:d} is {l_digit} and is"

if (l_digit > 5 and number > 0):
    print(f"{str} greater than 5")
elif (l_digit == 0):
    print(f"{str} 0")
else:
    print(f"Last digit of {number:d} is {-l_digit} and is less than 6 and not 0")
