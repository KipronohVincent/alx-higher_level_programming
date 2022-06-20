#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except (ZeroDivisionError, TypeError):
        print("Inside result: None")
        return None
    finally:
        print("Inside finally: {}".format(result))
