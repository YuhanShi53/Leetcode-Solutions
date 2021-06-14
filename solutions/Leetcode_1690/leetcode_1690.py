from itertools import accumulate
from typing import List


class Solution1:
    def stone_game_vii(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        prev_sum = [0] + list(accumulate(stones))

        def dfs(i, j):
            if i == j:
                return 0
            if dp[i][j] == 0:
                sum = prev_sum[j+1] - prev_sum[i]
                dp[i][j] = max(sum - stones[i] - dfs(i+1, j), sum - stones[j] - dfs(i, j-1))
            return dp[i][j]
        return dfs(0, n-1)
