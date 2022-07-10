# 1.4: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.

# Solution: p. 204

from typing import List


def zero_matrix(matrix: List[List[int]]) -> None:
    def zero_row(r: int) -> None:
        for c in range(col_count):
            matrix[r][c] = 0
    
    def zero_column(c: int) -> None:
        for r in range(row_count):
            matrix[r][c] = 0

    first_row_has_zero = first_col_has_zero = False
    row_count = len(matrix)
    col_count = len(matrix[0])

    for c in range(col_count):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break
    
    for r in range(row_count):
        if matrix[r][0] == 0:
            first_col_has_zero = True
            break

    for r in range(1, row_count):
        for c in range(1, col_count):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
    
    for c in range(col_count):
        if matrix[0][c] == 0:
            zero_column(c)
    
    for r in range(row_count):
        if matrix[r][0] == 0:
            zero_row(r)

    if first_row_has_zero:
        zero_row(0)
    
    if first_col_has_zero:
        zero_column(0)
