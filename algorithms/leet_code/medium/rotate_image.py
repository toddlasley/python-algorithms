# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# https://leetcode.com/problems/rotate-image/

from typing import List

def rotate_image(matrix: List[List[int]]) -> None:
    n = len(matrix)

    for level in range(n // 2):
        first = level
        last = n - level - 1

        for i in range(first, last):
            offset = i - first

            temp = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = matrix[first][i]
            matrix[first][i] = temp
