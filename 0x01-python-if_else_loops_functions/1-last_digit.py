#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = int(number_str[-1])
message = "Last digit of"
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print(f"{message} {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"{message} {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"{message} {number} is {last_digit} and is 0")
