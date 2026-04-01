#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("{:d} arguments.".format(count))
    elif count == 1:
        print("{:d} argument:".format(count))
    else:
        print("{:d} arguments:".format(count))
    for i in range(1, count + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
