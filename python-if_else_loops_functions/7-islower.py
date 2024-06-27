#!/usr/bin/python3

def islower(c):
    # Check if c is a single character and if its ASCII value falls within the range of lowercase letters
    return len(c) == 1 and ord('a') <= ord(c) <= ord('z')

def main():
    islower = __import__('7-islower').islower

    print("a is {}".format("lower" if islower("a") else "upper"))  # Output: a is lower
    print("H is {}".format("lower" if islower("H") else "upper"))  # Output: H is upper
    print("A is {}".format("lower" if islower("A") else "upper"))  # Output: A is upper
    print("3 is {}".format("lower" if islower("3") else "upper"))  # Output: 3 is upper
    print("g is {}".format("lower" if islower("g") else "upper"))  # Output: g is lower

if __name__ == "__main__":
    main()
