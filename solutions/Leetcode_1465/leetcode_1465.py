from typing import List


class Solution1:
    def max_area(self, h: int, w: int,
                 horizontalCuts: List[int],
                 verticalCuts: List[int]) -> int:
        hs = [0] + sorted(horizontalCuts) + [h]
        vs = [0] + sorted(verticalCuts) + [w]
        horizontal_max = max(hs[i]-hs[i-1] for i in range(1, len(hs)))
        vertical_max = max(vs[i]-vs[i-1] for i in range(1, len(vs)))
        return horizontal_max * vertical_max % (10**9+7)
