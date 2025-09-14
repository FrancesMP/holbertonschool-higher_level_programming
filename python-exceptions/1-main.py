#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

# Test 1: entier positif
value = 42
print("Return:", safe_print_integer(value))  # Affiche: 42 + Return: True

# Test 2: negative integer
value = -3
print("Return:", safe_print_integer(value))  # Affiche: -3 + Return: True

# Test 3: zero
value = 0
print("Return:", safe_print_integer(value))  # Affiche: 0 + Return: True

# Test 4: string
value = "abc"
print("Return:", safe_print_integer(value))  # Rien + Return: False

# Test 5: float
value = 3.14
print("Return:", safe_print_integer(value))  # Rien + Return: False

# Test 6: boolean
value = True
print("Return:", safe_print_integer(value))  # Affiche: 1 + Return: True

# Test 7: liste
value = [1, 2, 3]
print("Return:", safe_print_integer(value))  # Rien + Return: False

# Test 8: dictionnaire
value = {"a": 1}
print("Return:", safe_print_integer(value))  # Rien + Return: False

# Test 9: None
value = None
print("Return:", safe_print_integer(value))  # Rien + Return: False

