# Given a string s, find the length of the longest substring without repeating characters.

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def longest_nonrepeating_substring(s: str) -> int:
    seen_characters = dict()
    last_length = 0
    result = 0

    for i in range(len(s)):
        c = s[i]

        if c in seen_characters and seen_characters[c] > last_length:
            last_length = seen_characters[c]

        seen_characters[c] = i + 1

        current_length = i - last_length + 1
        
        if result < current_length:
            result = current_length

    return result
