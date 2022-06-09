# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
# rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# https://leetcode.com/problems/zigzag-conversion/

def zig_zag_conversion(s: str, rows: int) -> str:
    if rows == 1:
        return s
    
    result = ''

    row_and_diagonal_count = rows + rows - 2

    for i in range(rows):
        for j in range(i, len(s), row_and_diagonal_count):
            result = result + s[j]

            if i > 0 and i < rows - 1:
                k = j + row_and_diagonal_count - (2 * i)

                if k < len(s):
                    result = result + s[k]

    return result
