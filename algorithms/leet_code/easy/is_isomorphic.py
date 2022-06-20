# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.

# https://leetcode.com/problems/isomorphic-strings/submissions/

def is_isomorphic(s: str, t: str) -> bool:
    letters = dict()
    
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        if (s_char in letters and letters[s_char] != t_char) or (s_char not in letters and t_char in letters.values()):
            return False
        else:
            letters[s_char] = t_char
    return True
