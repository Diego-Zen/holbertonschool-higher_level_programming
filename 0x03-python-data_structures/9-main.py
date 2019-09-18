#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
my_list1 = []
my_list2 = [1, 90, 2, 13, 34, 100, -13, 3]
max_value = max_integer(my_list)
max_value1 = max_integer(my_list1)
max_value2 = max_integer(my_list2)
max_value3 = max_integer()
print("Max: {}".format(max_value))
print("Max: {}".format(max_value1))
print("Max: {}".format(max_value2))
print("Max: {}".format(max_value3))
