# 1.4: Given a string, write a function to check if it is a permutation of a palindrome.

# Solution: p. 195

def is_palindrome_permutation(s: str) -> bool:    
    letters = set()

    for i, x in enumerate(s):
        if x != ' ':
            if x in letters:
                letters.remove(x)
            else:
                letters.add(x)

    return len(letters) <= 1
