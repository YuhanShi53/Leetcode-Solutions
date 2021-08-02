from typing import List

class Solution1:
    def candy(self, ratings: List[int]) -> int:
        total = up = down = peak = 0
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                up += 1
                peak += up
                down = 0
                total += up + 1
            elif rating[i-1] == rating[i]:
                up = down = peak = 0
                total += 1
            else:
                up = 0
                down += 1
                total += 1 + down if down < peak else down
