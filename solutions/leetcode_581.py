""" Leetcode 581 - Shortest Unsorted Continuous Subarray

https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

1. Time: O(n) Memory: O(1)

"""

from typing import List


class Solution1:
    """ 1. MINE | Array """

    def find_unsorted_subarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        right = nums[-1]
        temp1 = len(nums) - 1
        i = len(nums) - 1
        while i > 0:
            if nums[i] - nums[i-1] < 0 and nums[i] < right:
                right = nums[i]
            if right - nums[i-1] < 0:
                temp1 = i - 1
            i -= 1
        if temp1 == len(nums) - 1:
            return 0

        left = nums[0]
        temp2 = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i+1] - nums[i] < 0 and nums[i] > left:
                left = nums[i]
            if left - nums[i+1] > 0:
                temp2 = i + 1
            i += 1
        return temp2 - temp1 + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 7, 9, 2, 11, 13, 15, 17, 6, 19, 21, 23]
    res = Solution1().find_unsorted_subarray(nums)
    print(res)
