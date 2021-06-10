import heapq
from collections import deque
from typing import List


class Solution1:
    def max_result(self, nums: List[int], k: int) -> int:
        q = deque(([(0, nums[0])]))
        ret = nums[0]
        for i in range(1, len(nums)):
            while q and q[-1][0] < (i - k):
                q.pop()
            ret = nums[i] + q[-1][1]
            while q and q[0][1] < ret:
                q.popleft()
            q.appendleft((i, ret))
        return ret


class Solution2:
    def max_result(self, nums, k):
        h = [(-nums[0], 0)]
        ret = nums[0]
        for i in range(1, len(nums)):
            while h and h[0][1] < (i-k):
                heapq.heappop(h)
            ret = -h[0][0] + nums[i]
            heapq.heappush(h, (-ret, i))
        return ret
