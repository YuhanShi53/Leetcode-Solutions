""" Leetcode 463 - Island Perimeter

https://leetcode.com/problems/island-perimeter/

1. self-implement Brute Force: Time: 776ms(23%) Memory: 14.1MB(50%)

"""
from typing import List


class Solution1:
    """ 1. self-implement: Brute Force """

    def island_perimeter(self, grid: List[List[int]]) -> int:
        prev_row = [0] * len(grid[0])
        count_cell = 0
        count_connect = 0
        for row in grid:
            prev_node = 0
            for i, x in enumerate(row):
                if x == 1:
                    count_cell += 1
                    if prev_node == 1:
                        count_connect += 1
                    if prev_row[i] == 1:
                        count_connect += 1
                prev_node = x
            prev_row = row
        perimeter = count_cell * 4 - count_connect * 2
        return perimeter


if __name__ == '__main__':
    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]
    res = Solution1().island_perimeter(grid)
    print(res)
