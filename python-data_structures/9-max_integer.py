#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # si la liste est vide
        return None

    maxint = my_list[0]  # commence avec le premier élément
    for i in my_list:    # parcours tous les éléments
        if i > maxint:
            maxint = i  # met à jour le max si i est plus grand
    return maxint
