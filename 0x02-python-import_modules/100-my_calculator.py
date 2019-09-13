#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    length = len(sys.argv)

    if length != 4:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)
    elif args[2] == "+" or args[2] == "-" or args[2] == "*" or args[2] == "/":
        num1 = int(args[1])
        num2 = int(args[3])
        if args[2] == "+":
            print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        elif args[2] == "-":
            print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        elif args[2] == "*":
            print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        elif args[2] == "/":
            print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
