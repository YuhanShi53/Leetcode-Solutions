""" Leetcode 198 - House Robber

https://leetcode.com/problems/house-robber/

1. SM Dynamic-Programmin: Time: O(n) Space: O(1)

"""

from typing import List


class Solution1:
    """ 1. SM Dynamic-Programming """

    def rob(self, nums: List[int]) -> int:
        profit_night_before = 0
        profit_last_night = 0

        for x in nums:
            temp = profit_last_night
            profit_last_night = max(profit_last_night, profit_night_before + x)
            profit_night_before = temp
        return profit_last_night


if __name__ == '__main__':
    nums = [1]
    res = Solution1().rob(nums)
    print(res)
