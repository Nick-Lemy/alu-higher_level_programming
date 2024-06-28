#!/usr/bin/python3
import  sys
if __name__ == "__main__":
   # print("{} arguments".format(len(sys.argv) - 1))
    if len(sys.argv) - 1 == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif len(sys.argv) - 1 == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
