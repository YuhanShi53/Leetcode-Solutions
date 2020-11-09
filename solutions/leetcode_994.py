""" Leetcode 994 - Rotting Oranges

https://leetcode.com/problems/rotting-oranges/

1. BFS: Time: O(n) Space: O(n)

"""

from collections import deque
from typing import List


class Solution1:
    """ 1. BFS """

    def oranges_roting(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        rotted_queue = deque()
        fresh_count = 0
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == 2:
                    rotted_queue.appendleft((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        num_day = 0
        while rotted_queue:
            num_day += 1
            num_rotted_today = len(rotted_queue)
            for i in range(num_rotted_today):
                x, y = rotted_queue.pop()
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if (0 <= new_x < num_row
                            and 0 <= new_y < num_col
                            and grid[new_x][new_y] == 1):
                        grid[new_x][new_y] = 2
                        rotted_queue.appendleft((new_x, new_y))
                        fresh_count -= 1

        return -1 if fresh_count > 0 else num_day - 1


if __name__ == '__main__':
    grid = [[1], [1], [1]]
    res = Solution1().oranges_roting(grid)
    print(res)
