# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.

# https://leetcode.com/problems/maximum-subarray/

from typing import List

def max_sub_array(nums: List[int]) -> int:
    current_sum = result = nums[0]

    for x in nums[1:]:
        current_sum = current_sum + x if current_sum + x > x else x
        result = max(result, current_sum)

    return result
