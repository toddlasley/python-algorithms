# Given an array arr[] of N distinct integers, the task is to check if this array is sorted when rotated counter-clockwise. 
# A sorted array is not considered sorted and rotated, i.e., there should at least one rotation.

# Input: arr[] = { 3, 4, 5, 1, 2} 
# Output: true 

# Input: arr[] = {7, 9, 11, 12, 5} 
# Output: true

# Input: arr[] = {7, 9, 11, 12} 
# Output: false


from typing import List


def is_sorted_rotated_array(nums: List[int]) -> bool:
    rotated_i = 0

    for i, x in enumerate(nums[1:], start=1):
        if nums[i - 1] > x:
            if rotated_i > 0:
                return False
            
            rotated_i = i
    
    if rotated_i == 0:
        return False
    
    n = len(nums)

    for i in range(1, n):
        real_i = (i + rotated_i) % n
        prev = (i - 1 + rotated_i) % n

        if nums[prev] > nums[real_i]:
            return False
      	
    return True