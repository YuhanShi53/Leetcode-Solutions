""" Leetcode 59 - Spiral Matric II

https://leetcode.com/problems/spiral-matrix-ii/

"""

from typing import List


class Solution1:
    def generate_matrix(self, n: int) -> List[List[int]]:
        """ 1. MINE | Straight-Forward """
        matrix = [[0 for _ in range(n)] for i in range(n)]
        visited = {}
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        x, y, idx = 0, 0, 0
        for value in range(1, n**2+1):
            matrix[y][x] = value
            visited[(x, y)] = True
            if (not 0 <= x + directions[idx][0] < n
                    or not 0 <= y + directions[idx][1] < n
                    or visited.get(
                        (x + directions[idx][0],
                         y + directions[idx][1]), False)):
                idx = (idx + 1) % 4
            x += directions[idx][0]
            y += directions[idx][1]
        return matrix


if __name__ == '__main__':
    n = 1
    matrix = Solution1().generate_matrix(n)
    print(matrix)
