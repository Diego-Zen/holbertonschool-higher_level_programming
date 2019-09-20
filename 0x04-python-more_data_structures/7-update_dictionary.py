#!/usr/bin/python3
def update_dictionary(a_dictionary: dict, key: str, value: any):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        new = {key: value}
        a_dictionary.update(new)
    return a_dictionary
