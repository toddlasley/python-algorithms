# Given a string s, return the longest palindromic substring in s.

# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longest_palindromic_substring(s: str) -> str:
        result = ''

        for i in range(len(s)):
            p1 = Solution.__find_palindrome_from_center(s, i, i)
            p2 = Solution.__find_palindrome_from_center(s, i, i + 1)

            p = p1 if len(p1) > len(p2) else p2

            if len(p) > len(result):
                result = p

        return result
    
    def __find_palindrome_from_center(s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        
        return s[left + 1:right]