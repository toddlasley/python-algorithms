# Given two strings s and t, return true if s is a subsequence of t,
# or false otherwise.

# A subsequence of a string is a new string that is formed from the
# original string by deleting some (can be none) of the characters without
# disturbing the relative positions of the remaining characters. (i.e.,
# "ace" is a subsequence of "abcde" while "aec" is not).

# https://leetcode.com/problems/is-subsequence/submissions/

from collections import deque


def is_subsequence(s: str, t: str) -> bool:
    queue = deque(s)

    i = 0
    while len(queue) != 0 and i < len(t):
        if queue[0] == t[i]:
            queue.popleft()
        i = i + 1

    return len(queue) == 0
