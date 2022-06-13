from typing import List

def insertion_sort(list: List[int]) -> List[int]:
    for i in range(1, len(list)):
        j = i

        while j > 0 and list[j] < list[j - 1]:
            temp = list[j]
            list[j] = list[j - 1]
            list[j - 1] = temp
            j = j - 1

    return list