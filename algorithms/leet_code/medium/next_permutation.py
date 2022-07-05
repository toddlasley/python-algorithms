# Given an array of integers nums, find the next lexicographically greater permutation of nums.

# https://leetcode.com/problems/next-permutation/

from typing import List


def next_permutation(nums: List[int]) -> None:
    def swap(i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(i: int) -> None:
        j = n - 1

        while i < j:
            swap(i, j)
            i += 1
            j -= 1

    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1

        while nums[j] <= nums[i]:
            j -= 1
        
        swap(i, j)

    reverse(i + 1)
