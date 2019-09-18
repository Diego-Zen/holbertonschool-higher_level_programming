#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        my_tuple = 0, None
        return my_tuple

    length = 0
    for i in sentence:
        length += 1

    my_tuple = length, sentence[0]
    return my_tuple
