from typing import List


class Solution1:
    def partition_disjoint(self, nums: List[int]) -> int:
        left_max = global_max = nums[0]
        partition = 0
        for i, x in enumerate(nums):
            if left_max > x:
                partition = i
                left_max = global_max
            global_max = max(global_max, x)
        return partition + 1
