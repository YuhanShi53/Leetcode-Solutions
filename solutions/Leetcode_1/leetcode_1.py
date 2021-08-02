from typing import List


class Solution1:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, x in enumerate(nums):
            diff = target - x
            if num_idx.get(diff, None) is not None:
                return [i, num_idx[diff]]
            else:
                num_idx[x] = i
