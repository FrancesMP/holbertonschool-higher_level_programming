#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Completes tuples with zeros if necessary
    a1, a2 = (tuple_a + (0, 0))[:2]  # Limit to 2 elements
    b1, b2 = (tuple_b + (0, 0))[:2]  # Limit to 2 elements

    # Adds the first and second elements
    return (a1 + b1, a2 + b2)
