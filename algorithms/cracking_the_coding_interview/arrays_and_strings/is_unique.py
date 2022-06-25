import enum


# 1.1: Implement an algorithm to determine if a string contains unique characters.

# Solution: p. 192

def is_unique(s: str) -> bool:
    characters = set()

    for i, x in enumerate(s):
        if x in characters:
            return False
        
        characters.add(x)

    return True
