#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys

    names = dir(hidden_4)

    for i in range(len(names)):
        if names[i][:1] != "_":
            print("{}".format(names[i]))
