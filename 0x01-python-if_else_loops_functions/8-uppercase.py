#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        asc = ord(str[i])
        if asc < 123 and asc > 96:
            asc -= 32
        print("{:c}".format(asc), end="")
    print()
