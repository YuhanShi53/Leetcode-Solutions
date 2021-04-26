from typing import List


class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-n//2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                    matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]


class Solution2:
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
