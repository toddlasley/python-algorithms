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
