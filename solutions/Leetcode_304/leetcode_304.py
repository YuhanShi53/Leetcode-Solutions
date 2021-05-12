from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        for row in range(1, len(matrix)):
            self._matrix[row][0] += self._matrix[row-1][0]
        for col in range(1, len(matrix[0])):
            self._matrix[0][col] += self._matrix[0][col-1]
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                self._matrix[row][col] += self._matrix[row][col-1] + \
                    self._matrix[row-1][col] - self._matrix[row-1][col-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        up = self._matrix[row1-1][col2] if row1 > 0 else 0
        left = self._matrix[row2][col1-1] if col1 > 0 else 0
        corner = self._matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self._matrix[row2][col2] - up - left + corner


if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    row1, col1, row2, col2 = 1, 1, 2, 2
    num_matrix = NumMatrix(matrix)
    ans = num_matrix.sumRegion(row1, col1, row2, col2)
    print(ans)
