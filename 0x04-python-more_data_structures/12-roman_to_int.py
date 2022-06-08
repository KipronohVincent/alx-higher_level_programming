#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a roman numeral to an integer
    You can assume the number will be between 1 to 3999.
    """
    if roman_string is None:
        return
    if len(roman_string) == 0:
        return
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_string = roman_string.upper()
    total = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
            total += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i - 1]]
        else:
            total += roman_dict[roman_string[i]]
    return total
