#!/usr/bin/python3
for i in range(1, 90):
    if i / 10 < i % 10 and i != 89:
        print("{:02d},".format(i), end=" ")
print("{:02d}".format(i))
