#!/usr/bin/python3

def print_last_digit(number):
    # Get the absolute value of the number to handle negative numbers
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
