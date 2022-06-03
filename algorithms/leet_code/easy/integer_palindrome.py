# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.

# https://leetcode.com/problems/palindrome-number/

from math import ceil, floor

def is_palindrome(n: int) -> bool:
    result = True
    
    if (n < 0):
        return False
    
    e = 0
    while (floor(n / 10 ** e)) >= 10:
        e = e + 1

    middle_degree = ceil(e / 2)

    if e % 2 != 0:
        middle_degree + 1

    for i in range(middle_degree):
        j = e - i

        front_digit_bound = floor(n / 10 ** (j + 1)) * 10 if j < e else 0
        front_digit = floor(n / 10 ** j)

        if front_digit_bound != 0:
            front_digit = front_digit - front_digit_bound

        back_digit = floor(n / 10 ** i) - floor(n / 10 ** (i + 1)) * 10

        if front_digit != back_digit:
            result = False
            break
    
    return result
