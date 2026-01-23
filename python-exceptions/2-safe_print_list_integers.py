#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):  # Vérifie si l'élément est un entier
                print("{:d}".format(my_list[i]), end='')
                count += 1
        except IndexError:
            break  # Sort de la boucle si l'index est en dehors de la liste
    print()  # Affiche une nouvelle ligne après tous les entiers
    return count