from typing import List


class Solution1:
    def max_count(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        ms, ns = zip(*ops)
        return min(ms) * min(ns)
