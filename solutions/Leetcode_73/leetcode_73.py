from typing import List


class Solution1:
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        col_0 = 1
        for i in range(num_rows):
            if matrix[i][0] == 0:
                col_0 = 0
            for j in range(1, num_cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(num_rows-1, -1, -1):
            for j in range(num_cols-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            matrix[i][0] = 0 if col_0 == 0 else matrix[i][0]
