import heapq
from typing import List


class Solution1:
    def furthest_building(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        for i in range(1, len(heights)):
            if heights[i] - heights[i-1] > 0:
                heapq.heappush(h, heights[i] - heights[i-1])
                if len(h) > ladders:
                    if h[0] <= bricks:
                        bricks -= heapq.heappop(h)
                    else:
                        return i - 1
        return len(heights) - 1
