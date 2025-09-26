#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    """
    list_division Divides element by element of two lists.

    This function takes two lists and attempts to divide each element in the
    first list by the corresponding element in the second list.
    The function ensures that the operation is safe (exceptions type, out of
    range, division by zero)

    Args:
        my_list_1 (_type_): The first list containing numerators.
        my_list_2 (_type_): The second list containing denominators.
        list_length (_type_): The number of elements to divide.

    Returns:
        list: List with result of each division
    """

    result_list = []

    for item in range(0, list_length):
        try:
            result_list.append(my_list_1[item] / my_list_2[item])
        except (TypeError):
            print("wrong type")
            result_list.append(0)

        except (ZeroDivisionError):
            print("division by 0")
            result_list.append(0)

        except (IndexError):
            print("out of range")
            result_list.append(0)

        finally:
            continue

    return result_list
