#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            # Vérifier si les éléments sont des nombres
            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                raise ValueError("wrong type")
            # Effectuer la division
            division_result = element_1 / element_2
            result.append(division_result)
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except ValueError as e:
            print(e)
            result.append(0)
        finally:
            continue
    
    return result
