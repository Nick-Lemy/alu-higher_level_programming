#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
prefix = "Last digit of {} is {} and is ".format(number, number[-1])

if int(number[-1]) < 6 and int(number[-1]) != 0 :
    print(prefix + "and is less than 6 and not 0")
elif int(number[-1]) > 5:
    print(prefix + "greater than 5")
elif int(number[-1]) == 0:
    print(prefix + "0")
