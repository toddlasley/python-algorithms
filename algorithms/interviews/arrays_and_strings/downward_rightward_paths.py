# Given an M x N matrix, return the number of unique paths one could take when trying to
# navigate from the top left position to the bottom right position while only being able
# to move downward and to the right.

from typing import List

def downward_rightward_paths(matrix: List[List[int]]) -> int:
    row_count = len(matrix)
    col_count = len(matrix[0])
    
    def traverse(r: int, c: int) -> int:
        if r >= row_count or c >= col_count:
            return 0
        elif r == row_count - 1 and c == col_count - 1:
            return 1
        else:
            return traverse(r + 1, c) + traverse(r, c + 1)
    
    return traverse(0, 0)
