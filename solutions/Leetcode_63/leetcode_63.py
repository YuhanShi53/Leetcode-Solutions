from typing import List


class Solution1:
    def unique_paths_with_obstacles(self, obstacleGrid):
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(col)]
        dp[0] = 1 - obstacleGrid[0][0]
        for i in range(1, col):
            dp[i] = dp[i-1] * (1 - obstacleGrid[0][i])
        for i in range(1, row):
            dp[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, col):
                dp[j] = (dp[j] + dp[j-1]) * (1 - obstacleGrid[i][j])
        return dp[-1]


class SolutionMINE:
    def unique_paths_with_obstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(col)] for j in range(row)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        queue = [(0, 0)]
        while queue:
            count = len(queue)
            while count:
                x, y = queue.pop()
                if obstacleGrid[x][y] != 1:
                    if x - 1 >= 0 and obstacleGrid[x-1][y] != 1:
                        dp[x][y] += dp[x-1][y]
                    if y - 1 >= 0 and obstacleGrid[x][y-1] != 1:
                        dp[x][y] += dp[x][y-1]

                    if x + 1 < row and obstacleGrid[x+1][y] != 1 and (x+1, y) not in queue:
                        queue.insert(0, (x+1, y))

                    if y+1 < col and obstacleGrid[x][y+1] != 1 and (x, y+1) not in queue:
                        queue.insert(0, (x, y+1))
                count -= 1
        return dp[row-1][col-1]
