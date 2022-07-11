# 1.9: Given two strings, write code to check if one is a rotated version
# of the other.

# Solution: p. 206

def is_rotated_string(s: str, t: str) -> bool:
    # easy
    # if len(s) != len(t):
    #     return False
    # else:
    #     return s in t + t

    # manually
    n = len(s)

    if n != len(t):
        return False
    
    i = 0

    for c in t + t:
        if s[i] == c:
            i += 1

            if i == n:
                break
        else:
            i = 0
    
    return i == n
