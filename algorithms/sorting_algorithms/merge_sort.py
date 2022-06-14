from math import floor
from typing import List


class MergeSort:
    def sort(l: List[int]) -> List[int]:
        MergeSort.__sort(l, 0, len(l) - 1)

        return l
    
    def __sort(l: List[int], low: int, high: int) -> None:
        if low >= high:
            return

        mid = floor(low + (high - low) / 2)
        MergeSort.__sort(l, 0, mid)
        MergeSort.__sort(l, mid + 1, high)
        MergeSort.__merge(l, low, mid, high)

        
    def __merge(l: List[int], low: int, mid: int, high: int) -> None:
        copy = list(l)

        k = i = low
        j = mid + 1

        while k <= high:
            if i > mid:
                l[k] = copy[j]
                j = j + 1
            elif j > high:
                l[k] = copy[i]
                i = i + 1
            elif copy[i] < copy[j]:
                l[k] = copy[i]
                i = i + 1
            else:
                l[k] = copy[j]
                j = j + 1

            k = k + 1
    