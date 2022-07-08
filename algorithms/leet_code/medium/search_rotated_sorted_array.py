# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index.
# Given the array nums after the possible rotation and an integer target, return the index
# of target if it is in nums, or -1 if it is not in nums.

# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

def search_rotated_sorted_array(nums: List[int], target: int) -> int:
    n = len(nums)
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    
    pivot = low
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        true_mid = (mid + pivot) % n

        if nums[true_mid] == target:
            return true_mid
        elif nums[true_mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
