#!/usr/bin/python3

def safe_print_division(a, b):

    """
    safe_print_division Function that divides 2 integers and prints the result.

    Args:
        a (_type_): number A
        b (_type_): number B

    Returns:
        int: Result of division
    """

    try:
        my_result = a / b
    except (ZeroDivisionError):
        my_result = None
    finally:
        print("Inside result: {}".format(my_result))
    return my_result
