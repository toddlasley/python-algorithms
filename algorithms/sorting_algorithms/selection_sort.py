from typing import List

def selection_sort(list: List[int]) -> List[int]:
    for i in range(len(list)):
        min_index = i

        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        
        min = list[min_index]
        list[min_index] = list[i]
        list[i] = min

    return list
