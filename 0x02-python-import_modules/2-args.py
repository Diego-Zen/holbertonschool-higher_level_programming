#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv
    length = len(sys.argv)
    argslen = length - 1

    if length == 1:
        print("{:d} {}".format(argslen, "arguments."))
    elif length == 2:
        print("{:d} {}".format(argslen, "argument:"))
        print("{:d}: {}".format(argslen, arguments[1]))
    else:
        print("{:d} {}".format(argslen, "arguments:"))
        for i in range(1, length):
            print("{:d}: {}".format(i, arguments[i]))
