#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

def test_safe_print_list():
    print("Test 1: Liste vide, x=3 (doit rien afficher, return 0)")
    result = safe_print_list([], 3)
    print("Returned:", result)
    print("---")

    print("Test 2: x non passé, par défaut x=0 (doit rien afficher, return 0)")
    result = safe_print_list([1, 2, 3])
    print("Returned:", result)
    print("---")

    print("Test 3: x = True (équivaut à 1, doit afficher 1 élément)")
    result = safe_print_list([10, 20, 30], True)
    print("Returned:", result)
    print("---")

    print('Test 4: my_list = "abc", x=2 (doit afficher "ab")')
    result = safe_print_list("abc", 2)
    print("Returned:", result)
    print("---")

    print("Test 5: x = 0 (doit rien afficher, return 0)")
    result = safe_print_list([1, 2, 3], 0)
    print("Returned:", result)
    print("---")

    print("Test 6: x négatif, ex: -5 (doit print message erreur et return None ou 0)")
    result = safe_print_list([1, 2, 3], -5)
    print("Returned:", result)
    print("---")

# Appelle la fonction de test
test_safe_print_list()


