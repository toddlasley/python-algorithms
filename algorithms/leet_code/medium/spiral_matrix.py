# Given an m x n matrix, return all elements of the matrix in spiral order.

# https://leetcode.com/problems/spiral-matrix/

from typing import List

def spiral_traversal(matrix: List[List[int]]) -> List[int]:
    def all_indeces_traversed() -> bool:
        return len(result) == r * c
    
    result = []

    r = len(matrix)
    c = len(matrix[0])
    r_start = 0
    r_end = r - 1
    c_start = 0
    c_end = c - 1

    while r_start <= r_end and c_start <= c_end:
        
        i = c_start
        
        while i <= c_end and not all_indeces_traversed():
            result.append(matrix[r_start][i])
            i += 1
        
        r_start += 1
        i = r_start

        while i <= r_end and not all_indeces_traversed():
            result.append(matrix[i][c_end])
            i += 1
        
        c_end -= 1
        i = c_end

        while i >= c_start and not all_indeces_traversed():
            result.append(matrix[r_end][i])
            i -= 1
        
        r_end -= 1
        i = r_end

        while i >= r_start and not all_indeces_traversed():
            result.append(matrix[i][c_start])
            i -= 1
        
        c_start += 1

    return result
