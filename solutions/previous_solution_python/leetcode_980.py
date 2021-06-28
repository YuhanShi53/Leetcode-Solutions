""" Leetcode 980 - Unique Paths III

https://leetcode.com/problems/unique-paths-iii/

1. MINE DFS & Backtracking: 

"""

from typing import List


class Solution1:
    """ 1. MINE DFS & Backtracking """

    def unique_paths_iii(self, grid: List[List[int]]) -> int:
        num_empty = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    num_empty += 1
                elif x == 1:
                    start_x = j
                    start_y = i
                elif x == 2:
                    end_x = j
                    end_y = i

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        height = i + 1
        width = j + 1
        path_count = 0

        def dfs(x, y, count, visited):
            nonlocal path_count

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if new_x == end_x and new_y == end_y:
                    if count == 0:
                        path_count += 1
                    else:
                        continue

                if (0 <= new_x < width
                        and 0 <= new_y < height
                        and grid[new_y][new_x] == 0):
                    grid[new_y][new_x] = -1
                    dfs(new_x, new_y, count - 1, visited + [(new_x, new_y)])
                    grid[new_y][new_x] = 0

        dfs(start_x, start_y, num_empty, [])
        return path_count


if __name__ == '__main__':
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    res = Solution1().unique_paths_iii(grid)
    print(res)
