# Given two binary strings a and b, return their sum as a binary string.

def binary_addition(a: str, b: str) -> str:
    result = ''
        
    i = len(a) - 1
    j = len(b) - 1
    remainder = 0

    while i >= 0 or j >= 0:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0
        
        s = x + y + remainder
        
        current = '0'
        
        if s >= 2:
            remainder = 1
        
            if s == 3:
                current = '1'
        elif s == 1:
            current = '1'
            remainder = 0
        
        
        result = current + result
        
        i -= 1
        j -= 1


    if remainder == 1:
        result = '1' + result

    return result
