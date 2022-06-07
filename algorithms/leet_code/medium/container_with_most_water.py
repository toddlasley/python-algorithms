from typing import List

def container_with_most_water(heights: List[int]) -> int:
    result = 0
    left = 0
    right = len(heights) - 1

    while (left < right):
        current_area = min(heights[left], heights[right]) * (right - left)

        if current_area > result:
            result = current_area

        if heights[left] < heights[right]:
            left = left + 1
        else:
            right = right - 1

    return result
