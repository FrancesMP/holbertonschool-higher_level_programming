#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence == "":
        first = None
    else:
        first = sentence[0]
    length = len(sentence)
    tuple1 = (length, first)
    return tuple1
