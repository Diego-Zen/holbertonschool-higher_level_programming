#!/usr/bin/python3
def no_c(my_string):
    my_list = []
    for i in my_string:
        if i == "C" or i == "c":
            continue
        my_list.append(i)
    new_string = ''.join(my_list)
    return new_string
