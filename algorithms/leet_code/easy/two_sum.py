# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# https://leetcode.com/problems/two-sum/

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    result = list()

    for i in range(len(nums) - 1):
        x = nums[i]

        for j in range(i + 1, len(nums)):
            y = nums[j]

            if (x + y == target):
                result.append(i)
                result.append(j)
                break

    return result