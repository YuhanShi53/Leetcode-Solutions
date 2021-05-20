from typing import List


class Solution1:
    def min_moves_2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(x-median) for x in nums)


class Solution2:
    def min_moves_2(self, nums):
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums)//2))