from typing import List


class Solution1:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, 0
        for i in range(len(cost)):
            prev1, prev2 = prev2, cost[i] + min(prev1, prev2)
        return min(prev1, prev2)
