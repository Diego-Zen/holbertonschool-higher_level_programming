#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list.sort()

    for idx, i in enumerate(my_list):
        if (idx > 0):
            if i == my_list[idx - 1]:
                continue
        sum += i
    return sum
