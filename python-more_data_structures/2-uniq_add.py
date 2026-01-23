#!/usr/bin/python3`
def uniq_add(my_list=[]):
    total = 0
    unique_numbers = []  # This list will keep track of unique integers
    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)  # Add to unique list
            total += number  # Add to total
    return total
