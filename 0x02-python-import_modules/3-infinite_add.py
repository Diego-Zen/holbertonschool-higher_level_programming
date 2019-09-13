#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv
    length = len(sys.argv)
    result = 0

    if length == 1:
        print("{:d}".format(length - 1))
    else:
        for i in range(1, length):
            result += int(arguments[i])
        print("{:d}".format(result))
