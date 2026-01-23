#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    total = 0
    length = len(roman_string)
    
    for i in range(length):
        value = roman_values[roman_string[i]]
        
        # Vérifier si le prochain caractère existe et si la valeur actuelle est inférieure à la suivante
        if i + 1 < length and value < roman_values[roman_string[i + 1]]:
            total -= value  # Soustraire si c'est un cas de soustraction
        else:
            total += value  # Ajouter sinon
    
    return total
