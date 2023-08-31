#!/usr/bin/python3

def safe_print_integer(value):
    try:
        formattedValue = "{:d}".format(value)
        print(formattedValue)
        return (True)
    except (ValueError, TypeError):
        return (False)
