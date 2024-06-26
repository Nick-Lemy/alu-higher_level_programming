#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_char = str(number)
cond = int(number_char[-1])
if number < 0:
    cond = -cond

prefix = "Last digit of {} is {} and is ".format(number, cond)

if cond < 6 and cond != 0:
    print(prefix + "less than 6 and not 0")
elif cond > 5:
    print(prefix + "greater than 5")
elif cond == 0:
    print(prefix + "0")
