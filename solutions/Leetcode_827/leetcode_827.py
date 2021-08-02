from collections import defaultdict, deque
from typing import List


class SolutionMINE:
    def largest_island(self, grid: List[List[int]]):
        zeros_adjacency = defaultdict(int)
        num_rows = len(grid)
        num_cols = len(grid[0])

        ones = []
        visited = {}
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    ones.append((i, j))

        if len(ones) == num_rows * num_cols:
            return num_rows * num_cols
        elif len(ones) == 0:
            return 1

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while ones:
            x, y = ones.pop()
            if visited.get((x, y), False):
                continue
            q = deque([(x, y)])
            visited[(x, y)] = True
            area = 0
            neighbour_zeros = []
            while q:
                x, y = q.pop()
                area += 1
                for dx, dy in directions:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < num_rows and 0 <= yy < num_cols:
                        if grid[xx][yy] == 1 and not visited.get((xx, yy), False):
                            visited[(xx, yy)] = True
                            q.appendleft((xx, yy))
                        elif grid[xx][yy] == 0 and (xx, yy) not in neighbour_zeros:
                            neighbour_zeros.append((xx, yy))
            for neighbour in neighbour_zeros:
                zeros_adjacency[neighbour] += area

        return max(zeros_adjacency.values()) + 1
