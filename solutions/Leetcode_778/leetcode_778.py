from collections import defaultdict
from typing import List


class Solution1:
    def swim_in_water(self, grid: List[List[int]]) -> int:
        time = defaultdict(list)
        time[grid[0][0]].append((0, 0))
        visited = set()
        n = len(grid)
        for t in range(n**2):
            while time[t]:
                x, y = time[t].pop()
                if x == y == n - 1:
                    return t
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    if (0 <= x+dx < n
                            and 0 <= y+dy < n
                            and (x+dx, y+dy) not in visited):
                        visited.add((x+dx, y+dy))
                        time[max(grid[x+dx][y+dy], t)].append((x+dx, y+dy))
