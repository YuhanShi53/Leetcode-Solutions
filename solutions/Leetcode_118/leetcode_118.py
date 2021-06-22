from typing import List


class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(numRows-1):
            row = [1] + [triangle[-1][i] + triangle[-1][i+1] for i in range(len(triangle)-1)] + [1]
            triangle.append(row)
        return triangle
