# 1.2: Given two strings, write a method to determine if one is
#       a permutation of the other.

# Solution: p. 193

def is_permutation(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    result = True
    letters = dict()

    for i, x in enumerate(s):
        if x in letters:
            letters[x] = letters[x] + 1
        else:
            letters[x] = 1

    for i, x in enumerate(t):
        if x not in letters or letters[x] - 1 < 0:
            return False
        else:
            letters[x] = letters[x] - 1
    
    return result
