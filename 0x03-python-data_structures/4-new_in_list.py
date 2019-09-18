#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    my_new_list = []

    for i in my_list:
        my_new_list.append(i)

    if idx < 0 or idx > length:
        return my_new_list

    my_new_list[idx] = element

    return my_new_list
