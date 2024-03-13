#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
check_negative = number < 0
print(f"Last digit of {number} is ", end="")
if check_negative:
    number = number * -1
out = number % 10
if check_negative:
    out = out * -1
if out > 5:
    print("{} and is greater than 5".format(out))
elif out == 0:
    print(f"{out} and is 0")
elif out < 6 and not 0:
    print(f"{out} and is less than 6 and not 0")
