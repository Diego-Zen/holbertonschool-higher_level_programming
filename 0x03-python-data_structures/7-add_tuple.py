#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_tuple_a = len(tuple_a)
    length_tuple_b = len(tuple_b)
    my_list_a = []
    my_list_b = []

    for i in range(length_tuple_a):
        my_list_a.append(tuple_a[i])
    for i in range(length_tuple_b):
        my_list_b.append(tuple_b[i])

    # print(my_list_a)
    # print(my_list_b)

    if length_tuple_a < 2:
        for i in range(length_tuple_a, 2):
            my_list_a.append(0)

    # print(my_list_a)

    if length_tuple_b < 2:
        for i in range(length_tuple_b, 2):
            my_list_b.append(0)

    # print(my_list_b)

    new_tuple = my_list_a[0] + my_list_b[0], my_list_a[1] + my_list_b[1]

    return new_tuple
