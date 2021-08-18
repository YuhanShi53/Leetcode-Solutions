from typing import List


class Solution1:
    def remove_boxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for i in range(n)] for j in range(n)]

        def helper(left, right, k):
            if left > right:
                return 0
            if dp[left][right][k] > 0:
                return dp[left][right][k]

            left_copy = left
            k_copy = k
            while left + 1 <= right and boxes[left] == boxes[left+1]:
                left += 1
                k += 1
            res = (k+1)**2 + helper(left+1, right, 0)
            for m in range(left+1, right+1):
                if boxes[m] == boxes[left]:
                    res = max(res, helper(left+1, m-1, 0) + helper(m, right, k+1))
            dp[left_copy][right][k_copy] = res
            return res

        return helper(0, len(boxes)-1, 0)


class Solution1_cache:
    def remove_boxes(self, boxes):
        from functools import lru_cache

        @lru_cache
        def helper(left, right, k):
            if left > right:
                return 0

            left_copy = left
            k_copy = k
            while left + 1 <= right and boxes[left] == boxes[left+1]:
                left += 1
                k += 1
            res = (k+1)**2 + helper(left+1, right, 0)
            for m in range(left+1, right+1):
                if boxes[m] == boxes[left]:
                    res = max(res, helper(left+1, m-1, 0) + helper(m, right, k+1))
            return res
        return helper(0, len(boxes)-1, 0)
