#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict):
    new_dict = sorted(a_dictionary.items())
    for tupl in new_dict:
        print("{}: {}".format(tupl[0], tupl[1]))
