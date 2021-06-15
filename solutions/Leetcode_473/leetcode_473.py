from typing import List


class Solution1:
    def make_square(self, matchsticks: List[int]) -> bool:
        def dfs(targets, idx):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                if matchsticks[idx] <= targets[i]:
                    targets[i] -= matchsticks[idx]
                    if dfs(targets, idx+1):
                        return True
                    targets[i] += matchsticks[idx]
            return False

        stick_sum = sum(matchsticks)
        if stick_sum % 4:
            return False
        targets = [stick_sum // 4] * 4
        matchsticks.sort(reverse=True)
        return dfs(targets, 0)
