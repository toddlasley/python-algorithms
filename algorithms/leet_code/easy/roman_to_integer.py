# Given a roman numeral, convert it to an integer.

# https://leetcode.com/problems/roman-to-integer/

def roman_to_integer(s: str) -> int:
    roman_numerals = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

    result = 0
    for i in reversed(range(len(s))):
        numeral_value = roman_numerals[s[i]]

        if i != len(s) - 1 and numeral_value < roman_numerals[s[i + 1]]:
            result = result - numeral_value
        else:
            result = result + numeral_value 
    
    return result
