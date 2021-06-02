from typing import List


class Solution1:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    current = 0
                    grid[i][j] = 0
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        current += 1
                        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                            if (0 <= x+dx < m
                                and 0 <= y+dy < n
                                and grid[x+dx][y+dy]):
                                grid[x+dx][y+dy] = 0
                                stack.append((x+dx, y+dy))
                    max_area = max(max_area, current)
        return max_area

class Solution2:
    def max_area_of_island(self, grid):
        m = len(grid)
        n = len(grid[0])
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                grid[x][y] = 0
                return 1 + dfs(x-1, y) + dfs(x, y-1) + dfs(x+1, y) + dfs(x, y+1)
            return 0
        return max([dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]] + [0])
