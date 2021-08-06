from typing import List


class Solution1:
    def stone_game(self, piles: List[int]) -> bool:
        num_piles = len(piles)
        dp = [[0] * num_piles for _ in range(num_piles)]
        for d in range(1, num_piles):
            for i in range(num_piles-d):
                dp[i][i+d] = max(piles[i] - dp[i+1][i+d], piles[i+d] - dp[i][i+d-1])
        return dp[0][-1] > 0
