#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        print("Inside result: None")
        return None
    else:
        print("Inside result: {:0.1f}".format(result))
        return result
    finally:
        pass
