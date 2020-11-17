""" Leetcode 845 - Longest Mountain in Array

https://leetcode.com/problems/longest-mountain-in-array/

"""

from typing import List


class Solution1:
    """ 1. MINE-Greedy """

    def longest_mountain(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        start = end = -1
        max_len = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                if start == -1 or start < end:
                    start = i
            elif nums[i] - nums[i-1] < 0:
                if start != -1:
                    end = i
                    max_len = max(max_len, end-start+2)
            else:
                start = end = -1
        return max_len


if __name__ == '__main__':
    nums = [2, 2, 2]
    res = Solution1().longest_mountain(nums)
    print(res)
