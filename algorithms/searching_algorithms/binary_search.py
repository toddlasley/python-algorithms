from typing import List


def binary_search(l: List[int], target: int) -> int:
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2

        if l[mid] == target:
            return mid
        elif l[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
